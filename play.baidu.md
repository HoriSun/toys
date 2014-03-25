javascript:(
    function(){
        function $$(name){return document.getElementsByClassName(name);};
        function find(listname,target){
            var p = $$(listname);
            for(i=0;i<p.length;i++)
                if(p[i].innerHTML==target)
                    return p[i];
            return null;
        }
        function kill(name){
            r=$$(name)[0];
            console.log(r);
            if(r!=undefined)
                r.remove();
        }
        kill('mb-layout-bd column4');
        kill('m-client-product');
        kill('down-mobile');
        find('text','播放记录').click();
        while($$('ui-reelList-songname')==[]);
        console.log($$('ui-reelList-songname'));
        (find('ui-reelList-songname','The Reluctant Heroes')).click();
        $$('wg-button')[1].click();
        $$('pause-ad-close')[0].click();
        document.getElementById('toptip').remove();
    }
)()
