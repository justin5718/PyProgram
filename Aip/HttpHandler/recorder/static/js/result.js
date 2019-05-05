$(document).ready(function(){
    $("h2#to").hide();
});
var dd;

var str = new String();

var s = new Array();

str = $("#to").text()
s = str.split(' ');

for (var i=0; i<s.length; i++){
    var txt = $("<b></b>").text(s[i]);
    $("#test").append(txt);
    $("#test").append(" ");
}

$('b').hover(
    function () {
        $("#222").empty();
        var d = $(this).text();
        qqq(d);
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
    console.log(str1);
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
            signType: "v3"
        },
        dataType: "jsonp",
        success: function (data) {
            console.log(data['basic']['explains']);
            var t = data['basic']['explains'];
            for (var i=0; i<t.length;i++){
               var txt = $("<h2></h2>").text(t[i]);
               $("#222").append(txt);
            }

        }
    });
    return x;
}




































