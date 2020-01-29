/////////////////////////////////////////////////////////////////////////////////////////////////
//
// author naotoshi morita
// create 2019/8/10
// explane this program is typing main program
//
/////////////////////////////////////////////////////////////////////////////////////////////////
//
// 初期処理
//
/////////////////////////////////////////////////////////////////////////////////////////////////
//-----------------------------------------------------------------------------------------------
//変数定義
//-----------------------------------------------------------------------------------------------
var str = "";                           //問題格納用配列
var str1 = "";                           //問題格納用配列
var a_true = "";                        //正解した文字列格納用
var a_remain = "";                      //残り文字数格納用
var ukey = "";                          //ユーザ入力キー格納用
var i = 0;                              //キーコード変換カウンター
var j = 0;                              //1行ごとの文字数カウンタ
var k = 0;                              //行数カウンタ
var n = 0;                              //合計数カウンタ　※「ｊ」カウンタから格納
var p = 0;                              //startボタンを1度だけ処理させる制御フラグ
var r = 0;                              //インデントスキップフラグ
var s = 0;                              //コンテンツリスト作成用ループカウンター
var t = 0;
var u = 0;
var miss = 0;
var typStart,typEnd;                    //開始時と終了時の時刻を格納
var cnt = 1;                            //キーコード変換カウンター範囲指定
var array = new Array();                //変換コード格納
var spArrayChild = [];                       //&nbsp;格納用
var spArrayParent = [];                       //spcount格納用配列
var htmlArrayChild = [];
var htmlArrayParent = [];
var strArray = [];                      //問題文変換コード格納用
var strArray1 = [];                      //問題文変換コード格納用
//-----------------------------------------------------------------------------------------------
//連想配列　入力キーコード対応表
//-----------------------------------------------------------------------------------------------
var obj = {
            " ":"32","!":"33","\"":"34","#":"35","$":"36","%":"37","&":"38","'":"39",
            "(":"40",")":"41","*":"42","+":"43",",":"44","-":"45",".":"46","/":"47","0":"48","1":"49",
            "2":"50","3":"51","4":"52","5":"53","6":"54","7":"55","8":"56","9":"57",":":"58",";":"59",
            "<":"60","=":"61",">":"62","?":"63","@":"64","A":"65","B":"66","C":"67","D":"68","E":"69",
            "F":"70","G":"71","H":"72","I":"73","J":"74","K":"75","L":"76","M":"77","N":"78","O":"79",
            "P":"80","Q":"81","R":"82","S":"83","T":"84","U":"85","V":"86","W":"87","X":"88","Y":"89",
            "Z":"90","[":"91","\\":"92","]":"93","^":"94","_":"95","`":"96","a":"97","b":"98","c":"99",
            "d":"100","e":"101","f":"102","g":"103","h":"104","i":"105",
            "j":"106","k":"107","l":"108","m":"109","n":"110","o":"111",
            "p":"112","q":"113","r":"114","s":"115","t":"116","u":"117",
            "v":"118","w":"119","x":"120","y":"121","z":"122","{":"123","|":"124","}":"125","~":"126"
            };
/////////////////////////////////////////////////////////////////////////////////////////////////
//
// 主処理
//
/////////////////////////////////////////////////////////////////////////////////////////////////
//-----------------------------------------------------------------------------------------------
//問題のリストを表示
//-----------------------------------------------------------------------------------------------
var client = new XMLHttpRequest();　                       //HMLHttpRequestで選択さたファイルをオーブンする。
client.open("GET", "content.txt", true);                   //取得したファイル名が選択できるように変更。
client.onload = function (e) {
  if (client.readyState === 4 && client.status === 200) {
      str1 = client.responseText;
      strArray1 = str1.split(/\r\n|\r|\n/);
      console.log(strArray1)
      for (s = 0; s < strArray1.length; s++) {
        console.log(s);
        sss = document.getElementById('sss');
        sss.insertAdjacentHTML('beforeend','<a href="#" id=' + s +' value="showID" onclick="getId(this);">' + strArray1[s] + '</a><br>');
      }
    } else {
      console.error(client.statusText);                         //ファイルが存在しなかったら
    }
};
client.onerror = function (e) {
  console.error(client.statusText);
};
client.send(null);
//-----------------------------------------------------------------------------------------------
//問題を選択したときのイベント
//-----------------------------------------------------------------------------------------------
function getId(ele) {
  var id_value = ele.id;                                        // eleのプロパティとしてidを取得
  console.log(id_value);
  var xhr = new XMLHttpRequest();　                             //HMLHttpRequestで選択さたファイルをオーブンする。
  xhr.open("GET", strArray1[id_value] + ".txt", true);          //取得したファイル名が選択できるように変更。
  xhr.onload = function (e) {
    if (xhr.readyState === 4 && xhr.status === 200) {
        str = xhr.responseText;
        strArray = str.split(/\r\n|\r|\n/);
        console.log(strArray);
        sss.parentNode.removeChild(sss);
        var ttt = document.getElementById('ttt');
        ttt.innerHTML = "start";       
      } else {
        console.error(xhr.statusText);                          //ファイルが存在しなかったら
      }
  };
  xhr.onerror = function (e) {
    console.error(xhr.statusText);
  };
  xhr.send(null);
}
//-----------------------------------------------------------------------------------------------
//問題を開始したときのイベント
//-----------------------------------------------------------------------------------------------
function OnLinkClick() {
  //1度だけ処理するフラグ
  if (p === 0) {
      //問題の行数分ループ
      for (var k = 0; k < strArray.length; k++) {
          //問題の1行文字数分ループ
          for ( var i = 0; i < strArray[k].length; i++) {
            if (r === 0 && strArray[k].substring(i,cnt) === " ") {
                //インデント対応
                //問題分のインデントを除去。
                //html上はインデントを表示させたいので、&nbsp;で置き換えを実行。
                spArrayChild[u] = "&nbsp;";
                cnt++;
                u++
            } else if (strArray[k].substring(i,cnt) === "<") {
                //特殊文字対応
                htmlArrayChild[t] = "&lt;";
                array.push(obj[strArray[k].substring(i,cnt)]);
                cnt++;
                r = 1;
                t++;
            } else if (strArray[k].substring(i,cnt) === ">") {
                //特殊文字対応
                htmlArrayChild[t] = "&gt;";
                array.push(obj[strArray[k].substring(i,cnt)]);
                cnt++;
                r = 1;
                t++;
            } else {
                //特殊文字以外
                htmlArrayChild[t] = strArray[k].substring(i,cnt);
                array.push(obj[strArray[k].substring(i,cnt)]);
                cnt++;
                r = 1;
                t++;
            }
          }
        t = 0;
        u = 0;
        r = 0;
        cnt = 1;
        spArrayParent.push(spArrayChild);       //2次元配列化
        htmlArrayParent.push(htmlArrayChild);   //2次元配列化
        spArrayChild = [];
        htmlArrayChild = [];
        strArray[k] = strArray[k].trim();
        // 要素の生成
        var toi = document.getElementById('toi');
        toi.insertAdjacentHTML('beforeend','<font  size="3" color="dimgray"><span id="a_true' + k + '"></span></font>' + 
                                           '<font  size="3" color="darkgray"><span id="a_remain' + k + '" style="background-color:lavender;"></span></font><br>');
        target = document.getElementById("a_true" + k);
        target.innerHTML = spArrayParent[k].slice().join("");
        target = document.getElementById("a_remain" + k);
        target.innerHTML = htmlArrayParent[k].slice().join("");
      }     
  }
  ttt.parentNode.removeChild(ttt); //start要素の削除
  p = 1;                           //処理フラグon
};
//-----------------------------------------------------------------------------------------------
//問題回答中の入力キーを受けるイベント
//-----------------------------------------------------------------------------------------------
document.onkeypress = keyPress;
//-----------------------------------------------------------------------------------------------
//問題実行中のイベント
//-----------------------------------------------------------------------------------------------
function keyPress() {
  //スタート時刻打刻
  if (n === 0) { 
    typStart = new Date();　　　　　                     // 実行時刻を記録
    k = 0;
  }
  ukey = event.keyCode;　　　　　　                      //入力キー格納
  //キー判定
  if (array[j + n] == ukey) {
    j++;
    a_true = htmlArrayParent[k].slice(0,j).join("");             //正解文字印字
    target = document.getElementById("a_true" + k); 
    target.innerHTML = spArrayParent[k].slice().join("") + a_true;
    a_remain = htmlArrayParent[k].slice(j).join("");　　　　　　　//残り文字印字
    target = document.getElementById("a_remain" + k); 
    target.innerHTML = a_remain;
      //1行の終わり判定
      if (strArray[k].length === j) {
          //全ての文字入力判定
          if (n + j === array.length) {
            /////////////////////////////////////////////////////////////////////////////////////////////////
            //
            //終了処理
            //
            /////////////////////////////////////////////////////////////////////////////////////////////////
            console.log("n==>" + n + "j==>" + j);
            toi.parentNode.removeChild(toi);　　　　　　　//要素の削除
            typEnd = new Date();                          //全文字入力していたら、終了時間を記録する
            var keika = typEnd - typStart;                //終了時間－開始時間で掛かったミリ秒を取得する
            var sec = Math.floor( keika/1000 );           //1000で割って「切捨て」、秒数を取得
            var msec = keika % 1000;                      //1000で割った「余り(%で取得できる）」でミリ秒を取得
            var finish="GAME終了　時間：" + sec + "秒" + msec;  //問題終了を告げる文字列を作成
            var fin = document.getElementById('fin');
            fin.innerHTML = finish;
            var finish="合計タイプ数：" + (j + n);              //問題終了を告げる文字列を作成
            var fin = document.getElementById('total');
            fin.innerHTML = finish;
            var finish="ミスタイプ数：" + miss;              //問題終了を告げる文字列を作成
            var fin = document.getElementById('miss');
            fin.innerHTML = finish;
          } else {
            k++;
            n = n + j;
            j = 0;
            alert("type enter");　　　　　　　　　　　　　//改行アナウンス
        }
      }
  } else {
  　miss++
  }
};