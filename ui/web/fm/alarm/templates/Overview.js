!function(){var e=Handlebars.template,a=NOC.templates.fm_alarm=NOC.templates.fm_alarm||{};a.Overview=e({compiler:[7,">= 4.0.0"],main:function(e,a,l,n,t){var r,s=null!=a?a:{},u=l.helperMissing,m="function",p=e.escapeExpression;return"<b>"+p((r=null!=(r=l.subject||(null!=a?a.subject:a))?r:u,typeof r===m?r.call(s,{name:"subject",hash:{},data:t}):r))+"</b><br/>\n<pre>"+p((r=null!=(r=l.body||(null!=a?a.body:a))?r:u,typeof r===m?r.call(s,{name:"body",hash:{},data:t}):r))+"</pre>\n"},useData:!0})}();Ext.define("NOC.fm.alarm.templates.Overview", {});