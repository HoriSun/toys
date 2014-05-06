javascript:(
    function test(){
        function $$(name){
            return document.getElementsByClassName(name);
        };        
        function find(listname,target){
            var p = $$(listname);
            for(i=0;i<p.length;i++)
                if(p[i].innerHTML==target)
                    return p[i];
            return null;
        };
        
        function kill(name){
            k=$$(name);
            for(i=0;i<k.length;i++){
                r=k[i];
                if(r!=undefined)
                    r.remove();
            }
        }; 
        
        function filt(func,list){
            for(i=0;i<list.length;i++)
                func(list[i]);
        };

        
        
        function filter(f,a){
            b = [];
            for(i=0;i<a.length;i++)
                if(f(a[i]))
                    b.push(a[i]);
            return b;
        };
        
        function map(f,a){
            b = [];
            for(i=0;i<a.length;i++)
                b.push(f(a[i]));
            return b;
        };
        
        function killById(k){
            map(function(x){if(x.remove!=undefined)x.remove();},
                filter(function(x){if(x.id.match(k))return true;return false;},
                       document.getElementsByTagName('div')))
        };
        
        killById(/BAIDU/);
    
        
        
        
        kill('mb-layout-bd column4');
        kill('m-client-product');
        kill('down-mobile');
        if(find('text','播放记录')!=null)
            find('text','播放记录').click();
        while($$('ui-reelList-songname')==[]);
        if(find('ui-reelList-songname','The Reluctant Heroes')!=null)
            (find('ui-reelList-songname','The Reluctant Heroes')).click();
        if($$('wg-button').length)
            $$('wg-button')[1].click();
        if($$('pause-ad-close').length)
            $$('pause-ad-close')[0].click();
        if(document.getElementById('toptip'))
            document.getElementById('toptip').remove();
        filt(function(targ){targ.remove();},document.getElementsByTagName('iframe'));    
    }
)()