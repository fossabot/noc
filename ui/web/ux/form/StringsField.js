//---------------------------------------------------
// Ext.ux.form.StringsField
//     ExtJS4 form field
//     Embedded grid
//---------------------------------------------------
// Copyright (C) 2007-2015 The NOC Project
// See LICENSE for details
//---------------------------------------------------
Ext.define("Ext.ux.form.StringsField", {
    extend: "Ext.form.FieldContainer",
    mixins: {
        field: 'Ext.form.field.Field'
    },
    alias: "widget.stringsfield",

    initComponent: function() {
        var me = this;

        me.store = Ext.create("Ext.data.Store", {
            fields: ["value"],
            data: []
        });

        me.addButton = Ext.create("Ext.button.Button", {
            text: "Add",
            glyph: NOC.glyph.plus,
            scope: me,
            handler: me.onAddRecord
        });

        me.deleteButton = Ext.create("Ext.button.Button", {
            text: "Delete",
            glyph: NOC.glyph.minus,
            disabled: true,
            scope: me,
            handler: me.onDeleteRecord
        });

        me.grid = Ext.create("Ext.grid.Panel", {
            layout: "fit",
            store: me.store,
            columns: [
                {
                    text: "Value",
                    dataIndex: "value",
                    flex: 1,
                    editor: "textfield",
                    renderer: NOC.render.htmlEncode
                }
            ],
            plugins: [
                Ext.create("Ext.grid.plugin.CellEditing", {
                    clicksToEdit: 2,
                    listeners: {
                        scope: me,
                        edit: me.onCellEdit
                    }
                })
            ],
            dockedItems: [
                {
                    xtype: "toolbar",
                    dock: "top",
                    items: [
                        me.addButton,
                        me.deleteButton
                    ]
                }
            ],
            listeners: {
                scope: me,
                select: me.onSelect
            }
        });

        Ext.apply(me, {
            items: [
                me.grid
            ]
        });
        me.currentSelection = undefined;
        me.callParent();
    },

    getValue: function() {
        var me = this,
            value = [];
        me.store.each(function(r) {
            value.push(r.get("value"));
        });
        return value;
    },

    setValue: function(v) {
        var me = this;
        if(v === undefined || v === "") {
            v = [];
        } else {
            v = v.map(function(x) {
                return {
                    value: x
                }
            });
        }
        me.store.loadData(v);
        return me.mixins.field.setValue.call(me, v);
    },
    //
    onSelect: function(grid, record, index) {
        var me = this;
        me.currentSelection = index;
        me.deleteButton.setDisabled(false);
    },
    //
    onAddRecord: function() {
        var me = this,
            rowEditing = me.grid.plugins[0];
        rowEditing.cancelEdit();
        me.grid.store.insert(0, {});
        rowEditing.startEdit(0, 0);
    },
    //
    onDeleteRecord: function() {
        var me = this,
            sm = me.grid.getSelectionModel(),
            rowEditing = me.grid.plugins[0];
        rowEditing.cancelEdit();
        me.grid.store.remove(sm.getSelection());
        if(me.grid.store.getCount() > 0) {
            sm.select(0);
        } else {
            me.deleteButton.setDisabled(true);
        }
    },
    //
    onCellEdit: function(editor, e) {
        var me = this,
            editor = e.grid.columns[e.colIdx].getEditor();
        if(editor.rawValue) {
            e.record.set(e.field + "__label", editor.rawValue);
        }
    }
});