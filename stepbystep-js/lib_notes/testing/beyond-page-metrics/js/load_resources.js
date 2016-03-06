/**
 * Created by patrick on 15/11/11.
 */
(function(){
    var dom,doc,where,iframe=document.createElement("iframe");
    iframe.src='javascript:false';
    (iframe.frameElement || iframe).style.cssText = "width:0;height:0;border:0;display:none;";
    where=document.getElementsByTagName('script')[0]
    where.parentNode.insertBefore(iframe,where);
    try{
        doc=iframe.contentWindow.document
    }catch(e){
        dom=document.domain
        iframe.src="javascript:var d=document.open();" +
            "d.domain='"+dom+"';void(0)";
        doc=iframe.contentWindow.document;
    }

    doc.open()._l=function(){
        var js = this.createElement("script");
        if(dom) this.domain=dom;
        js.id="boomr-if-as";
        js.src = 'https://c.go-mpulse.net/boomerang/' + '24NZM-B6VZ9-PPXQV-ZEDGN-26VWA';
        BOOMR_lstart=new Date().getTime();
        this.body.appendChild(js);
    }
})();