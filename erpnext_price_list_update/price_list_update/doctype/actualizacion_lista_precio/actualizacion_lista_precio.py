# -*- coding: utf-8 -*-
# Copyright (c) 2017, Diamo and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils.background_jobs import enqueue
from frappe.model.document import Document


class ActualizacionListaPrecio(Document):

    def before_submit(self):
        enqueue(update_prices, queue='long', timeout='8000', actualizacion=self)


def update_prices(actualizacion):
    """
    Actualiza los Item Price de las listas de precios elegidas
    por el porcentaje definido
    """
    item_prices = frappe.get_all('Item Price', {'price_list': ('IN', [pl.price_list for pl in actualizacion.price_list])}, 'name')
    item_price_names = tuple([str(p.name) for p in item_prices])

    if len(item_price_names) == 1:
        item_price_names = item_price_names[0]
        query = """
            UPDATE `tabItem Price`
            SET price_list_rate = (price_list_rate + (price_list_rate * {percentage} ) / 100)
            WHERE name = "{item_price_names}";
        """.format(percentage=10, item_price_names=item_price_names)
    else:
        query = """
            UPDATE `tabItem Price`
            SET price_list_rate = (price_list_rate + (price_list_rate * {percentage} ) / 100)
            WHERE name IN {item_price_names};
        """.format(percentage=actualizacion.percentage, item_price_names=item_price_names)

    frappe.db.sql(query, as_dict=1)
    frappe.db.commit()


@frappe.whitelist()
def get_listas(tipo):
    if tipo == "selling":
        return frappe.get_all('Price List', {'selling': 1}, ['name'])
    elif tipo == "buying":
        return frappe.get_all('Price List', {'buying': 1}, ['name'])
    return frappe.get_all('Price List', ['name'])
