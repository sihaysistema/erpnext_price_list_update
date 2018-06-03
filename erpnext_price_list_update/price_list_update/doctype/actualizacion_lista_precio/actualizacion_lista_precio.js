// Copyright (c) 2017, Diamo and contributors
// For license information, please see license.txt

frappe.ui.form.on('Actualizacion Lista Precio', {
	refresh: function(frm) {
		if (frm.doc.docstatus != 1) {
			frm.add_custom_button(__("Traer Listas de Ventas"), function() {
	            frappe.call({
	                method: "erpnext_price_list_update.price_list_update.doctype.actualizacion_lista_precio.actualizacion_lista_precio.get_listas",
	                args: {
	                    tipo: 'selling'
	                },
	                callback: function(r, rt) {
	                    if (r.message) {
	                    	agregar_listas(frm, r.message)
	                    }
	                }
	            });
	        });

	        frm.add_custom_button(__("Traer Listas de Compras"), function() {
	            frappe.call({
	                method: "erpnext_price_list_update.price_list_update.doctype.actualizacion_lista_precio.actualizacion_lista_precio.get_listas",
	                args: {
	                    tipo: 'buying'
	                },
	                callback: function(r, rt) {
	                    if (r.message) {
	                        agregar_listas(frm, r.message)
	                    }
	                }
	            });
	        });

	        frm.add_custom_button(__("Traer Todas"), function() {
	            frappe.call({
	                method: "erpnext_price_list_update.price_list_update.doctype.actualizacion_lista_precio.actualizacion_lista_precio.get_listas",
	                args: {
	                    tipo: 'all'
	                },
	                callback: function(r, rt) {
	                    if (r.message) {
	                        agregar_listas(frm, r.message)
	                    }
	                }
	            });
	        });
		}
	}
});

function agregar_listas(frm, listas) {
	frm.doc.price_list = []
	for (var i in listas) {
	   	var row = frappe.model.add_child(frm.doc, frm.fields_dict.price_list.df.options, frm.fields_dict.price_list.df.fieldname);
	   	row.price_list = listas[i]['name'];
   	}
   	frm.refresh_field('price_list');
}