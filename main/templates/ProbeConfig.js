//---------------------------------------------------------------------
// {{pname}} Probe Config
//---------------------------------------------------------------------
// Generated by ./noc update-probe-form
//---------------------------------------------------------------------
// Copyright (C) 2007-{{year}} The NOC Project
// See LICENSE for details
//---------------------------------------------------------------------
console.debug("Defining {{extcls}}");

Ext.define("{{extcls}}", {
    extend: "NOC.core.ProbeConfig",
    form: [
        {% for v in pvars %}
        {
            name: "{{v.name}}",
            xtype: "{{v.xtype}}",
            fieldLabel: "{{v.fieldLabel}}",
            allowBlank: {% if v.allowBlank %}true{% else %}false{% endif %}
        }{{v.sep}}{% endfor %}
    ]
});