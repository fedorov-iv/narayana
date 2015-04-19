$(document).ready(function() {
    $('.answer').addClass('hidden');
    $("#publics_body a").addClass("links_in_body");
    $("#news_body a").addClass("links_in_body");
    $("#page_content a").addClass("links_in_body");
    var img_height = $("img#photo_full_img").attr('height');
    var top = ((550 - img_height) / 2) + "px";
    $("img#photo_full_img").css({'margin-top': top});
    
    $("div.pview_lenta").css({overflow: 'hidden'});
    var $allLi     = $("li.pview_lenta");
    var $liWidth   = 140;
    var $imgMargin = 2;

    $("img.pview_lenta").each(function(index){
    var $imgWidth = $(this).width();
    var $leftMargin  = ($liWidth - $imgWidth) / 2+'px';
        $(this).css({'margin-left': $leftMargin});
    })

    var $MovToLeft  = $("img.pview_lenta_left_nav");
    var $MovToRight = $("img.pview_lenta_right_nav");
    var $divWidth = $("div.pview_lenta");
        $divWidth.css({width: $liWidth * 3 + $imgMargin});
        $allLi.eq(0).css({left: 0});
        $allLi.eq(1).css({left: $liWidth });
        $allLi.eq(2).css({left: $liWidth * 2 });

    $MovToLeft.bind("click", function(){
    var $allLi = $("li.pview_lenta");
        $allLi.eq(0).insertAfter('ul.pview_lenta li:last');
    	$allLi.eq(0).css({left: 0 });
        $allLi.eq(1).css({left: $liWidth });
        $allLi.eq(2).css({left: $liWidth * 2 });
    });
    
    $MovToRight.bind("click", function(){
    var $allLi = $("li.pview_lenta");
        $allLi.eq(length - 1).insertBefore($allLi.eq(0));
    	$allLi.eq(0).css({left: 0 });
        $allLi.eq(1).css({left: $liWidth });
        $allLi.eq(2).css({left: $liWidth * 2 });
    });        
})

function PGshowImage(ImPath, ImW, ImH) {
    var $image = $("img#photo_full_img");
    var $top = ((550 - ImH) / 2) + "px";
    $image.fadeOut(1000).queue(function() {
        $image.attr({
            'src': ImPath, 
            'width': ImW, 
            'height': ImH
        })
        .css('margin-top', $top).dequeue();
    })
    .fadeIn(1000);
}

function showBlock(id) {
    $('#'+id).slideToggle('slow');
}

function OpenBigPic (fn, w, h) {
    window.open (fn, "bigpic", "width=600,height=600,resizable=no");
}



function onoff(id) {
    var el_id     = id;
    var sub_el_id = id + "a";
	var el        = document.getElementById(el_id);
	var sub_el    = document.getElementById(sub_el_id);
	el.style.display = (el.style.display == 'block')?'none':'block';
	sub_el.style.display = (sub_el.style.display == 'block')?'none':'block';
}

  var cssFix = function(){
  var u = navigator.userAgent.toLowerCase(),
  addClass = function(el,val){
    if(!el.className) {
      el.className = val;
    } else {
      var newCl = el.className;
      newCl+=(" "+val);
      el.className = newCl;
    }
  },
  is = function(t){return (u.indexOf(t)!=-1)};
  addClass(document.getElementsByTagName('html')[0],[
    (!(/opera|webtv/i.test(u))&&/msie (\d)/.test(u))?('ie ie'+RegExp.$1)
      :is('firefox/2')?'gecko ff2'
      :is('firefox/3')?'gecko ff3'
      :is('gecko/')?'gecko'
      :is('opera/9')?'opera opera9':/opera (\d)/.test(u)?'opera opera'+RegExp.$1
      :is('konqueror')?'konqueror'
      :is('applewebkit/')?'webkit safari'
      :is('mozilla/')?'gecko':'',
    (is('x11')||is('linux'))?' linux'
      :is('mac')?' mac'
      :is('win')?' win':''
  ].join(" "));
}();


$(function(){
  //Get our elements for faster access and set overlay width
  var div = $('div.video_lenta'),
               ul = $('ul.video_lenta'),
               // unordered list's left margin
               ulPadding = 10;

  //Get menu width
  var divWidth = div.width();

  //Remove scrollbars
  div.css({overflow: 'hidden'});

  //Find last image container
  var lastLi = ul.find('li:last-child');

  //When user move mouse over menu
  div.mousemove(function(e){

    //As images are loaded ul width increases,
    //so we recalculate it each time
    var ulWidth = lastLi[0].offsetLeft + lastLi.outerWidth() + ulPadding;

    var left = (e.pageX - div.offset().left) * (ulWidth-divWidth) / divWidth;
    div.scrollLeft(left, 'slow');
  });
});

function openWin(page, w, h) {
  var features;
  var top = (screen.height - h)/2, left = (screen.width - w)/2;
  if(top < 0) top = 0;
  if(left < 0) left = 0;
  features = 'top=' + top + ',left=' +left;
  features += ',height=' + h + ',width=' + w + ',location=no,menubar=no,toolbar=no,status=no,resizable=no';
  myWin = open(page, 'displayWindow', features);
}
