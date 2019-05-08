$(document).ready(function(){
    $("#to").hide();
});
var dd,e;

var str = new String();

var s = new Array();

str = $("#to").text();
skc = $("#from").text();
if(skc == "err_no:3301"){
    alert("无法识别，请重新输入语音");
    window.location.href="/recorder/";
}
//alert(str);
s = str.split(' ');
ddd(s);
//console.log(typeof s);


for (var i=0; i<s.length; i++){

    var txt = $("<span style='font-size: 28px'></span>").text(s[i]);
    $("#list").append(txt);
    $("#list").append(" ");
    $("#list").append(" ");
    $("#list").append(" ");
}

$('span').hover(
    function () {
        $("#222").empty();
        var d = $(this).text();
        qqq(d);
        fa(d);
    },
    function () {
    }
)

function getInput(input) {
    if(input.length == 0){
        return null
    }
    var result;
    var len = input.length;
    if(len < 20)
        result = input;
    else{
        var startstr = input.substring(0,10);
        var endstr = input.substring(len-10,len);
        result = startstr + endstr;
    }
    return result
}

//youdao api
function qqq(word){
    APP_ID = "3de4b4207bc5dd42";
    APP_KEy = "7N2gEi3lzDkrubcZjrm40jUeSwgTydIu";
    var salt = new Date().getTime();
    var curtime = Math.round(new Date().getTime()/1000);
    var query = word;
    var from = "auto";
    var to = "zh-CHS";
    var str1 = APP_ID + getInput(query) + salt + curtime + APP_KEy;
    var sign = sha256(str1);
    var x;
    //console.log(str1);
    $.ajax({
        url: 'http://openapi.youdao.com/api',
        type: 'POST',
        headers: {

        },
        data: {
            q: query,
            appKey: APP_ID,
            salt: salt,
            from: from,
            to: to,
            curtime: curtime,
            sign: sign,
            signType: "v3",
            ext: 'mp3'
        },
        dataType: "jsonp",
        success: function (data) {
            console.log(data['basic']['explains']);
            var t = data['basic']['explains'];
            var ph = data['basic']['phonetic'];
            phtxt = $('<span></span>').text("发音: ( "+ ph + " )");
            $("#222").append(phtxt);
            //$("#tospeak").attr("crossOrigin","anonymous");
            //var is = document.getElementById("tospeak");
            //is.play();
            //console.log(e);
            for (var i=0; i<t.length;i++){
               var txt = $("<h4></h4>").text(t[i]);
               $("#222").append(txt);
            }

        }
    });
    return x;
}
function fa(word) {
    //plays = $('<span class="glyphicon glyphicon-copyright-mark"></span>');
    //plays.attr("id", word);
    var ss = "/static/mp3/" + word + ".mp3";
    //alert(ss);
    aa=$("<audio autoplay='autoplay'></audio>");
    aa.attr("src",ss);
    $("#222").append(aa);
    $("#222").append(plays);
}


//后端下载语音文件“.mp3”
function ddd(list) {
    //console.log(list)
    $.ajax({
        url:'/recorder/download/',
        data: {
            "wordList": list
        },
        dataType: "json",
        type: "POST",
        traditional: true,
        success: function (data) {
            if(data == "1")
                alert("failed");
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
                    // 状态码
                    console.log(XMLHttpRequest.status);
                    // 状态
                    console.log(XMLHttpRequest.readyState);
                    // 错误信息
                    console.log(textStatus);
                }
    });
}


































