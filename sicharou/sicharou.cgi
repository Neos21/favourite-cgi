#!/usr/local/bin/perl

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++　　[ あいさつ、しちゃ朗!! ]
#+++		･････>>> All Created by Tacky
#+++		･････>>> Copyright (c) 1999.6 Tacky's Room. All rights reserved....
#+++        Homepage >>> http://tackysroom.com/
#+++
#+++ 設置方法構成(具体例)
#+++
#+++ public_html（ホームページディレクトリ）
#+++ |
#+++ |-- cgi-bin（任意のディレクトリ）
#+++   |
#+++   |-- jcode.pl      (755)…(日本語ライブラリ)
#+++   |-- sicharou.cgi  (755)…(スクリプト本体)
#+++   |-- sicharou.txt  (666)…(ログファイル)…空のままアップロード
#+++   |-- sicharou2.txt (666)…(投稿回数管理ファイル)…空のままアップロード
#+++   |-- sicharou3.txt (666)…(常連様用メッセージ格納ファイル)…空のままアップロード
#+++
#+++ 　　■( )内はパーミッッションの値です。
#+++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

require './jcode.pl';										#日本語コード変換

$script 			= "./sicharou.cgi";						#<<<このスクリプトの名前
$method 			= "POST";								#<<<METHODの指定（POSTで動作しなかったら、GET)
$logfile 			= "./sicharou.txt";						#<<<メッセージのログファイル名
$logfile2 			= "./sicharou2.txt";					#<<<メッセージを登録してくれた方の登録回数累計を保持するファイル　※昇進を使わない場合は''
$logfile3 			= './sicharou3.txt';					#<<<メッセージを登録してくれた方々への人別メッセージを登録するファイル
$lockfile			= './sicharou.lock';					#<<<ロックファイルの名前を指定

$title  			= "『挨拶・しちゃ朗』";					#<<<タイトルを指定
$titlelogo 			= "./sicharou.gif";		#<<<上段部にタイトルロゴを指定する場合、フルパスで指定。指定しない場合は「""」
$bgcolor			= "#ffffff";							#<<<背景色
$backpicture 		= "../s-1-yellow.gif";			#<<<背景に画像を表示する場合、フルパスで指定。

$tbgcolor			= '#ffcc00' ;							#<<<入力フォームの背景色
$submit 			= "おはこんば～♪" ;					#<<<入力フォームの「送信」ボタンに表示される文字

#============================================================================================================================================
#(iMODEの場合)
$i_name_sz			= 16 ;									#<<<名前欄の文字数
$i_email_sz			= 16 ;									#<<<Email欄の文字数
$i_hp_sz			= 16 ;									#<<<Homepage欄の文字数
$i_message_sz1		= 16 ;									#<<<メッセージ欄の文字数
$i_message_sz2		= 3 ;									#<<<メッセージ欄の行数※１行テキストの場合は対象外
$title_i			= '*挨拶しちゃ朗!!!*';						#タイトルを指定
$titlelogo_i		= '';									#タイトル画像を指定
$titlelogo_w		= 95 ;									#<<<タイトル画像の横幅(pixel)
$titlelogo_h		= 16 ;									#<<<タイトル画像の縦幅(pixel)
$i_bgcolor			= '#ffff66' ;							#<<<投稿内容を表示する場合の背景色
$i_txcolor			= '#000000' ;							#<<<投稿内容を表示する場合の文字色
$i_disp				= 1 ;									#<<<初期表示時にレス記事を簡易表示とする？(0:no 1:yes)
$pagemax_i			= 3 ;									#imode時、１ページ内に表示する件数(親記事の件数)
$textflg_i			= 2 ;									#<<<メッセージ欄の形状。（1:１行テキスト　2:複数行テキスト）
$emailflg_i			= 1 ;									#<<<メールアドレスを入力する？(0:しない 1:する)
$hpflg_i			= 1 ;									#<<<ＵＲＬを入力する？(0:しない 1:する)

#(Webの場合)
$w_name_sz			= 20 ;									#<<<名前欄の文字数
$w_email_sz			= 20 ;									#<<<Email欄の文字数
$w_hp_sz			= 20 ;									#<<<Homepage欄の文字数
$w_message_sz1		= 40 ;									#<<<メッセージ欄の文字数
$w_message_sz2		= 5 ;									#<<<メッセージ欄の行数※１行テキストの場合は対象外
$cellheadbgcolor	= "#99CC00";							#<<<メッセージ表示部分のセル背景色
$cellbgcolor1 		= "#ffffcc";							#<<<メッセージ表示部分のセル背景色１
$cellbgcolor2 		= "#ffcc33";							#<<<メッセージ表示部分のセル背景色２（１と２で繰り返し表示される）
$pagemax 			= 30 ;									#<<<１ページ内に表示する件数
$tsz				= '90%';								#<<<ログ表示部のテーブル横サイズ
$textflg			= 2 ;									#<<<メッセージ欄の形状。（1:１行テキスト　2:複数行テキスト）
$emailflg			= 1 ;									#<<<メールアドレスを入力する？(0:しない 1:する)
$hpflg				= 1 ;									#<<<ＵＲＬを入力する？(0:しない 1:する)

#============================================================================================================================================
$textcolor    		= "#990000";							#<<<メッセージ表示部分のテキスト文字色
$linkcolor		    = "#cc6600";							# リンク色（未読リンク）
$vlinkcolor			= "#666666";							# リンク色（既読リンク）
$alinkcolor	 		= "#ff3300";							# リンク色（押した時）
$pt					= '10pt';								#全体のフォントサイズ（pt指定以外何があるのか、僕知らない。(^^ゞ）

$url 				= "http://tackysroom.com";				#<<<戻り先のURL
$password 			= "pass";								#<<<管理者メンテナンス用パスワード（ログ編集用））
$kanriname			= "abcde";								#<<<管理者の名前（ここに指定された名前は、ランキング対象外となります）
$datamax 			= 300 ;									#<<<最大データ保存件数
$messagemax 		= 50 ;									#<<<来訪者用メッセージの最大件数
$manual 			= 0 ;									#<<<管理人からのﾒｯｾｰｼﾞを表示する？(0:no 1:入力ﾌｫｰﾑの下に表示 2:画面下部に表示)

#↓アイコンの指定。$icon_gif[3]...[10]のように適当に増やして下さいね。	※imodeではアイコンは表示出来ません
$icon_flg			= 'yes';								#投稿時にアイコンを使用するか？
#↓管理者用アイコンとパスワードを指定。管理人は１つしかアイコン登録出来ません。
#  $oiconpassに指定したパスワードで投稿した場合、$oicon_gifのアイコンが表示されるようになってます。
#その下は、画像サイズ。_wは幅。_hは高さです。わからない場合は_wの方だけ0にしておいてね。
#管理者アイコンは特に必要無い場合は、$oiconpass = '';として下さい。
$oicon_gif	  = './d_ahiru.gif' ;		$oiconnm  = 'password';
$oicon_gif_w = 32 ; $oicon_gif_h = 32 ;

#↓常連者用アイコンと投稿時の名前を指定。$jicon_gif[2]...[5]のように適当に増やして下さいね。
#  $jiconnmに指定した名前で投稿した場合、$jicon_gifのアイコンが表示されるようになってます。
#その下は、画像サイズ。_wは幅。_hは高さです。わからない場合は_wの方だけ0にしておいてね。
$jicon_gif[0] = './kuma.gif' ;		$jiconnm[0] = 'Ａさん' ;
$jicon_gif_w[0] = 38 ; $jicon_gif_h[0] = 38 ;
$jicon_gif[1] = './parappa.gif' ;	$jiconnm[1] = 'Ｂさん';
$jicon_gif_w[1] = 37 ; $jicon_gif_h[1] = 35 ;

$icon_imode			= 7	;	#imodeからのアクセスの場合、固定で１個だけ下記のアイコンの番号を選択してください。

#訪問者用アイコンとアイコンの名前の指定。$icon_gif[3]...[10]のように適当に増やして下さいね。
#その下は、画像サイズ。_wは幅。_hは高さです。わからない場合は_wの方だけ0にしておいてね。
$icon_gif[0] = './ball.gif' ;		$iconnm[0] = 'ボール' ;
$icon_gif_w[0] = 32 ; $icon_gif_h[0] = 32 ;
$icon_gif[1] = './corgi.gif' ;		$iconnm[1] = 'コーギー' ;
$icon_gif_w[1] = 32 ; $icon_gif_h[1] = 32 ;
$icon_gif[2] = './cow.gif' ;		$iconnm[2] = 'うし' ;
$icon_gif_w[2] = 32 ; $icon_gif_h[2] = 32 ;
$icon_gif[3] = './denchi.gif' ;	$iconnm[3] = '電池' ;
$icon_gif_w[3] = 32 ; $icon_gif_h[3] = 32 ;
$icon_gif[4] = './dorayaki.gif' ;	$iconnm[4] = 'ドラ焼き' ;
$icon_gif_w[4] = 32 ; $icon_gif_h[4] = 32 ;
$icon_gif[5] = './duck.gif' ;		$iconnm[5] = 'あひる' ;
$icon_gif_w[5] = 32 ; $icon_gif_h[5] = 32 ;
$icon_gif[6] = './h_bambi.gif' ;	$iconnm[6] = 'バンビ' ;
$icon_gif_w[6] = 32 ; $icon_gif_h[6] = 32 ;
$icon_gif[7] = './h_bear.gif' ;	$iconnm[7] = 'くま' ;
$icon_gif_w[7] = 32 ; $icon_gif_h[7] = 32 ;
$icon_gif[8] = './h_kaeru.gif' ;	$iconnm[8] = 'かえる' ;
$icon_gif_w[8] = 32 ; $icon_gif_h[8] = 32 ;
$icon_gif[9] = './h_momo.gif' ;	$iconnm[9] = 'モモ' ;
$icon_gif_w[9] = 32 ; $icon_gif_h[9] = 32 ;
$icon_gif[10] = './h_saru.gif' ;	$iconnm[10] = 'さる１号' ;
$icon_gif_w[10] = 32 ; $icon_gif_h[10] = 32 ;
$icon_gif[11] = './h_usagi.gif' ;	$iconnm[11] = 'うさ１号' ;
$icon_gif_w[11] = 32 ; $icon_gif_h[11] = 32 ;
$icon_gif[12] = './kappa.gif' ;	$iconnm[12] = 'かっぱ' ;
$icon_gif_w[12] = 32 ; $icon_gif_h[12] = 32 ;
$icon_gif[13] = './mail.gif' ;		$iconnm[13] = 'メール' ;
$icon_gif_w[13] = 32 ; $icon_gif_h[13] = 32 ;
$icon_gif[14] = './monkey1.gif' ;	$iconnm[14] = 'さる２号' ;
$icon_gif_w[14] = 32 ; $icon_gif_h[14] = 32 ;
$icon_gif[15] = './nachan.gif' ;	$iconnm[15] = 'なっちゃん' ;
$icon_gif_w[15] = 32 ; $icon_gif_h[15] = 32 ;
$icon_gif[16] = './oyaji.gif' ;	$iconnm[16] = 'オヤジ' ;
$icon_gif_w[16] = 32 ; $icon_gif_h[16] = 32 ;
$icon_gif[17] = './panda.gif' ;	$iconnm[17] = 'パンダ' ;
$icon_gif_w[17] = 32 ; $icon_gif_h[17] = 32 ;
$icon_gif[18] = './poch.gif' ;		$iconnm[18] = 'ポチ' ;
$icon_gif_w[18] = 32 ; $icon_gif_h[18] = 32 ;
$icon_gif[19] = './risu.gif' ;		$iconnm[19] = 'りす' ;
$icon_gif_w[19] = 32 ; $icon_gif_h[19] = 32 ;
$icon_gif[20] = './ebi.gif' ;		$iconnm[20] = '海老' ;
$icon_gif_w[20] = 32 ; $icon_gif_h[20] = 32 ;
$icon_gif[21] = './tamago.gif' ;	$iconnm[21] = '玉子' ;
$icon_gif_w[21] = 32 ; $icon_gif_h[21] = 32 ;
$icon_gif[22] = './takoyaki.gif' ;	$iconnm[22] = 'たこ焼き' ;
$icon_gif_w[22] = 32 ; $icon_gif_h[22] = 32 ;
$icon_gif[23] = './tulip.gif' ;	$iconnm[23] = 'チューリップ' ;
$icon_gif_w[23] = 32 ; $icon_gif_h[23] = 32 ;
$icon_gif[24] = './usa2.gif' ;		$iconnm[24] = 'うさ２号' ;
$icon_gif_w[24] = 32 ; $icon_gif_h[24] = 32 ;
$icon_gif[25] = './volley.gif' ;	$iconnm[25] = 'バレーボール' ;
$icon_gif_w[25] = 32 ; $icon_gif_h[25] = 32 ;

#アイコン一覧を表示する際、１行にアイコンを何個表示します？
$icon_line					= 5 ;	#←の場合、５個表示したら改行するって事です。

#<<<Webからのアクセス時、画面下部に表示する管理者からのメッセージ。"EOM"～EOMの行までに必ず入れてください。メッセージ不要の場合は、$manualmsgの行からEOMの行まで全て削除してね
$manualmsg = <<"EOM";
<table border=0 width=50%  cellspacing=0 cellpadding=5><tr><td bgcolor=#ffffcc>
おはこんばー！僕「しちゃ朗」は何かと\申\しますと、コミュニケーションを
とる為にとっても大切な事、そう!!『挨拶』です!!....挨拶しましょ～！ただそれだけ。（笑）
<br>僕の使い方は「名前を書いて、ポン♪　押すだけぇ～♪」で～す</font>
<br><font size=2 color=#333333> ※補足：『おはこんば～♪』は、みなさんがいつ挨拶してくれるか
わからないから、「おはよう」、「こんにちは」、「こんばんわ」をミックスしてみました～♪（笑）</font>
<br><b><font size=+1>iModeでも見られます</font></b>
</td></tr></table>
EOM

#<<<imodeからのアクセス時、画面下部に表示する管理者からのメッセージ。"EOM"～EOMの行までに必ず入れてください。メッセージ不要の場合は、$manualmsg2の行からEOMの行まで全て削除してね
$manualmsg2 = <<"EOM";
みんな気軽に書き込みしてね～♪
EOM

#◆◆◆↓セキュリティ◆◆◆
$postchk		= 1;		#投稿時・メンテナンス時のMethodをPOST限定にする場合は１。以外は０。
$urlchk			= '';	#ここで指定されたアドレス(CGIの設置アドレスを記入)以外から投稿があった場合をエラーとします。設定しない場合は''

$urllink		= 2 ;		#タイトル及び本文にhttpからのリンクがあったらエラーにする？
							#(0:しない 1:URLは全てする 2:以下の$urlerrで指定された文字が含まれているURLのみエラーとする
#↓$urllink=2の場合、以下に指定した文字を含むURLをエラーとする
$urlerrnm[0]	= 'exe';
$urlerrnm[1]	= 'virus';
$kaigyo			= 0;		#指定値分の改行が連続した場合、１行改行に置換します。　※指定しない場合は0
$name_comment	= 'coxmment';#定期的に投稿してくるような事があったらこの名前を適当に変えてみて下さい。自動投稿スクリプトの種類によっては全然意味無いけど。
@errword 		= ('','');	#投稿禁止語句　ex.@errword = ('死ね','テストテスト');
$urlcnt			= 2;		#メッセージ欄に記入出来るURLの個数　※指定しない場合は0
$japan			= 1;		#メッセージ欄に"全角文字/半角カナ(但し半角カナは文字化けする事もあります)"が１文字でも無ければエラーとする？(0:no 1:yes)
$mailerr		= 0;		#メアド欄を入力されたらエラーにする？(0:no 1:yes)　※自動書込ツールはメアドを指定してくる事が多い為あえてエラーとしてみる
$urlerr			= 0;		#URL欄を入力されたらエラーにする？(0:no 1:yes)　※自動書込ツールはURLを指定してくる事が多い為あえてエラーとしてみる
#◆◆◆↑セキュリティ◆◆◆

#スクロールバーの色変更。よくわからない方は、"EOM"の次の行から先頭がEOMの行の間を削除してね。
$scrollbar = <<"EOM";
BODY{
scrollbar-base-color : #eeeeee;
}
EOM

$tag				= 'no';									#タグ許可(yes,no)
@errtag = ('table','meta','form','!--','embed','html','body','tr','td','th','a');		#デンジャラ～なタグ

#=============================================================================================================================================================================================
#フォームＣＳＳ設定　("EOM"～EOMの間にメッセージを書いてください）
#※使用しない場合は、$css_style = "";とし、そこから２行(先頭がEOMの行までを)を削除して下さい。
$css_style = <<"EOM";
STYLE=font-size:$pt;color:#0f642d;background-color:#ffffcc;border-style:solid;border-color:#4d9900;border-width:1;
EOM

#▼枠を丸くする場合、初期設定では背景色を白以外にすると綺麗に表示されないです。＜色に合った透過画像を作る必要があります。作り方は「書き込み隊」の説明ページをみてね。
$maru						= 0 ;	#入力フォームの四角枠を丸くしますか？ (0:no 1:yes) ※Webのみ
$top_l						= './top_l_h.gif';			#メッセージ部左上隅の透過画像を指定※四角枠を丸くしない場合は対象外
$top_r						= './top_r_h.gif';			#メッセージ部右上隅の透過画像を指定※四角枠を丸くしない場合は対象外
$bottom_l					= './bottom_l_h.gif';		#メッセージ部左下隅の透過画像を指定※四角枠を丸くしない場合は対象外
$bottom_r					= './bottom_r_h.gif';		#メッセージ部右下隅の透過画像を指定※四角枠を丸くしない場合は対象外

$rankcnt					= 20 ;	#ランキング上位何人をランキング一覧画面に表示しますか？

#お祝いカウント設定。指定した投稿回数に達すると、お祝いメッセージを表示します。不要の場合は、@OIWAIの行を削除してね。
@OIWAI = (0,2,10,30,50,80,120,170,230,300,400,600,1000,1500,2500,4000);
$oiwaibgcolor = "#CC0000";	#お祝いカウントの場合の背景色
$oiwaitxcolor = "#ffffff";	#お祝いカウントの場合の文字色
#お祝いメッセージ表示の際の文章。NAMEとCNTの部分にはその人の名前と達成回数が置換されますので、
#必ずNAME・CNTという文字は入れておいてください。
$oiwaimsg = "<font size=+1>NAMEさん!!   投稿回数がCNT回に達成し昇進しました!!!!!</font>";

$oiwaitxcolor_i = "#000000";	#お祝いメッセージの文字色（携帯）
$oiwaimsg_i = "NAMEさん投稿回数がCNT回で昇進しました!";	#お祝いメッセージ(携帯)

#掲示板荒らし対策。排除したいプロバのアドレスを設定して下さい。
#　"xxx?.com"とした場合、"xxx1.com","xxx2.com"等、「？」の部分が文字列１つと判断します
#  "xxx*.com"とした場合、"xxx1.com","xxx12345.com等、「＊」の部分が０個以上の文字列と判断します。
#例：@DANGER_LIST=("xxx.com","yyy.com","zzz*.or.jp");
@DANGER_LIST=("","","");

#掲示板荒らし対策その２。メッセージ最大文字数を指定。特に設定しない場合は、''として下さい。
$maxword = '1000' ;

$renchan1		= 0 ;		#指定分以内の連続投稿はｴﾗｰとする。設定しない場合は0としてね。
$renchan2		= 0 ;		#指定回数以上の連続投稿はｴﾗｰとする。設定しない場合は0としてね。

$method 			= "POST";								#<<<METHODの指定（POSTで動作しなかったら、GET)

#↓上記にある「@OIWAI」に指定した回数で昇進していきます。@OIWAIと同じ個数分設定して下さい。
@rank	= ('幼稚園生','小学校低学年','小学校中学年','小学校高学年','中学生','高校生','大学生','平社員','係長','課長','部長','常務','専務','社長','会長');
#↓昇進に画像を使う場合、昇進回数と同じ個数分設定してください。※$rankicon[n]は必ず「0」から始まります。画像を使わない部分は''としてね。
#　画像の幅・高さがわからない人は、$rankicon_w[n] = 0 ; $rankicon_h[n] = 0 ;のように「0」として下さい。
$rankicon[0] = '' ;	$rankicon_w[0] = 0 ; $rankicon_h[0] = 0 ;
$rankicon[1] = '' ;	$rankicon_w[1] = 0 ; $rankicon_h[1] = 0 ;
$rankicon[2] = '' ;	$rankicon_w[2] = 0 ; $rankicon_h[2] = 0 ;
$rankicon[3] = '' ;	$rankicon_w[3] = 0 ; $rankicon_h[3] = 0 ;
$rankicon[4] = './madogiwa.gif' ;	$rankicon_w[4] = 32 ; $rankicon_h[4] = 32 ;
$rankicon[5] = './hantyou.gif' ;	$rankicon_w[5] = 32 ; $rankicon_h[5] = 32 ;
$rankicon[6] = './syunin.gif' ;	$rankicon_w[6] = 32 ; $rankicon_h[6] = 32 ;
$rankicon[7] = './taityou.gif' ;	$rankicon_w[7] = 32 ; $rankicon_h[7] = 32 ;
$rankicon[8] = './kakarityou.gif' ;	$rankicon_w[8] 	= 32 ; $rankicon_h[8] = 32 ;
$rankicon[9] = './katyou.gif' ;		$rankicon_w[9] 	= 32 ; $rankicon_h[9] = 32 ;
$rankicon[10] = './butyou.gif' ;	$rankicon_w[10] = 32 ; $rankicon_h[10] = 32 ;
$rankicon[11] = './zyoumu.gif' ;	$rankicon_w[11] = 32 ; $rankicon_h[11] = 32 ;
$rankicon[12] = './senmu.gif' ;		$rankicon_w[12] = 32 ; $rankicon_h[12] = 32 ;
$rankicon[13] = './syatyou.gif' ;	$rankicon_w[13] = 32 ; $rankicon_h[13] = 32 ;
$rankicon[14] = './kaityou.gif' ;	$rankicon_w[14] = 32 ; $rankicon_h[14] = 32 ;

$damedame		= 0 ;	#Locationヘッダが使えないサーバーは1。通常は0でいいはず。※トクトク、3nopage,WinNTサーバー等が1かな。

$frame_home			= '';			#[HOME]押下時のターゲット指定。フレームページを使っていない人はそのままでいいです。
$frame_other		= '';			#[昇進状態][一括レス]等の押下時のターゲット指定。フレームページを使っていない人はそのままでいいです。

$passsw			= 1;		#入力フォームにパスワード欄を付ける？(0:no 1:yes)　付けたら投稿者も自分の記事を修正、削除出来ますよ
$host_disp		= 0;		#リモートホストを表示する？(0:no 1:yes)
#投稿時のパスワードをcrypt関数を使用する（暗号化）
#crypt関数が利用出来ない場合もありますので、投稿時にエラーになる場合は、「0:使用しない」にして下さいね。
$ango			= 1 ;	#0:使用しない 1:使用する　（推奨：１：使用する）

$dsp_new		= 1;		#携帯ｱｸｾｽ時、「新規投稿ﾌｫｰﾑ」を別画面で表示する？(0:no 1:yes)

#<<<　ここから下はいじらない方が身のためです。(^_^;
utime time(), time(), __FILE__; 								# スクリプト生成日時の更新

#■■■Webからのアクセスからか携帯からのアクセスかを判断
$agent = $ENV{'HTTP_USER_AGENT'};
if( $agent =~ /Docomo/i ) {	$env = 1; }
elsif ( $agent =~ /UP.Browser/i) {	$env = 2; }
elsif ( $agent =~ /J-PHONE|Vodafone|SoftBank/i ) {	$env = 3; }
else	{	$env = 0 ; }
if ( $env != 0 )	{
	$acs		= 	1 ;
	$name_sz	= 	$i_name_sz ;
	$email_sz	= 	$i_email_sz	;
	$hp_sz		= 	$i_hp_sz	;
	$title 		= 	$title_i ;
	$titlelogo	= 	$titlelogo_i ;
	$message_sz1 = 	$i_message_sz1 ;
	$message_sz2 = 	$i_message_sz2	;
	$pagemax 	=	$pagemax_i ;
	$textflg	= 	$textflg_i ;
	$textflg2	= 	$textflg2_i ;
	$emailflg	=	$emailflg_i ;
	$hpflg		= 	$hpflg_i ;
}	else	{
	$acs		= 0 ;
	$name_sz	= 	$w_name_sz ;
	$email_sz	= 	$w_email_sz	;
	$hp_sz		= 	$w_hp_sz	;
	$message_sz1 = 	$w_message_sz1 ;
	$message_sz2 = 	$w_message_sz2	;
}
if ($acs == 1 ) { $css_style = "" ; $scrollbar = "" }

###<--- システム日時・時刻取得 ------------------------------------
$ENV{'TZ'} = "JST-9";
$iday = time - ( $renchan1 * 60 ) ;  #$renchan1分前
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime($iday);
$year = sprintf("%02d",$year + 1900);$month= sprintf("%02d",$mon + 1);$mday = sprintf("%02d",$mday);
$hour = sprintf("%02d",$hour);$min  = sprintf("%02d",$min);$sec  = sprintf("%02d",$sec);
$renday = "$year$month$mday $hour:$min";

($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
$year = sprintf("%02d",$year + 1900);$month = sprintf("%02d",$mon + 1);$mday = sprintf("%02d",$mday);
$hour = sprintf("%02d",$hour);$min = sprintf("%02d",$min);
$today = "$year$month$mday $hour:$min";

###############################################################################
#### Main Process  START  #####################################################
###############################################################################
#<<<COOKIEの取得
&cookieget;
#<<<フォームデコード＆変数代入
&decode ;
if ( $FORM{'action'} eq "maintenance" ) {      			#<<<"処理"がメンテナンスの場合
	&Maintenance;
}	elsif	( $FORM{'action'} eq "update" )		{		#<<<ログファイル更新
	&update ;
}	elsif	( $FORM{'action'} eq "update2" )	{		#<<<来訪者用メッセージファイル更新
	&update2 ;
}	elsif	( $FORM{'action'} eq "ranking" )	{		#<<<ランキング表示
	&ranking ;
}	elsif	( $FORM{'action'} eq "download" )	{		#<<<ダウンロード
	&download ;
}	elsif   ( $FORM{'action'} eq "icondisp" )	{		#<<<アイコン一覧表示
	&icondisp ;
}	elsif   ( $FORM{'action'} eq "info" )	{			#<<<昇進資格説明
	&info ;
}	elsif   ( $FORM{'action'} eq "input" )	{			#<<<入力フォームの表示
	&header ;
	&header2 ;
	&inputform ;
	&footer ;						   			#<<< htmlフッターの出力
}	else	{
	if ( $FORM{'action'} eq "regist" ) {	   			#<<<"処理"が登録の場合
	 	&regist; 								#ログ登録処理
		if ( $acs == 0 )	{
			if ( $damedame == 0 )	{
				print "Location: $script?\n\n";
			}	else	{
				print "Content-type: text/html\n\n";
				print "<html><head><META HTTP-EQUIV=\"Refresh\" CONTENT=\"0; URL=";
				print "$script?\">";
				print $dmy_tok2_cookie; # クッキーの発効
				print "</head><body></body></html>\n\n";
			}
			exit;
		}	else	{
			&cookieget;
		}
		&dataread ;
	}
	&header ;
	&header2 ;
	if ( $env == 0 || ($env != 0 && $dsp_new == 0) ) {
		&inputform;
	}
	&disp ;							   			#<<<登録済メッセージの表示
	if ( $manual == 2 )	{	&setumei;	}	#<<<「使い方」の表示
	print "</center>\n" if ( $acs == 0 );
	print "<br><br>\n";
	print "<div align=right>" if ( $acs == 0 ) ;
	print "<form action=\"$script\" method=\"$method\">\n";
	if ( $acs == 0 ) { print "No&nbsp;\n";	}
	print "<input type=text name=\"no\" size=3 $css_style>\n";
	if ( $acs == 1 ) { print "No<br>\n";	}
	if ( $acs == 0 ) { print "&nbsp;Pass&nbsp;\n";	}
	print "<input type=password name=\"pass\" size=5 $css_style>\n";
	if ( $acs == 1 ) { print "Pass<br>\n";	}
	print "<select name=proc $css_style>\n";
	print "<option value=\"edit\">編集";
	print "<option value=\"delete\">削除";
	print "<option value=\"message\">訪問者メッセージ";
	print "</select>\n";
	if ( $acs == 1 ) { print "<br>\n";	}
	print "<input type=hidden name=\"action\" value=\"maintenance\">\n";
	print "<input type=submit value=\"ADMIN\" $css_style>\n";
	#<<<　↓消さないでネ♪
	print "<br>\n";
	if ( $env == 0 ) {
		print "<a href=http://tackysroom.com target=_top>sicharou(Ver0.996)-Tacky\'s Room</a>\n";
	}	else	{
		print "<!-- sicharou Ver0.996 Created by Tacky\'s Room (URL:http://tackysroom.com) -->\n";
	}
	print "</form>";
	print "</div>\n" if ( $acs == 0 );
	&footer ;						   			#<<< htmlフッターの出力
}
###############################################################################
#### Main Process  END  #######################################################
###############################################################################

###<--------------------------------------------------------------
###<---   デコード＆変数代入
###<--------------------------------------------------------------
sub decode{
	if ($ENV{'REQUEST_METHOD'} eq "POST") {
		read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});$post=1;
	} else { $buffer = $ENV{'QUERY_STRING'};$post=0; }
	@pairs = split(/&/,$buffer);
	@msg = ();
	foreach $pair (@pairs) {
		($name, $value) = split(/=/, $pair);
		$value =~ tr/+/ /;
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		if ($tag eq 'yes') {
	        #危険なタグは禁止!!!
			foreach ( @errtag )	{
				if ($value =~ /<$_(.|\n)*>/i) {&error("使用出来ないタグが入力されています");}
			}
		}
		$value =~ s/(\r\n){$kaigyo,}/$1/g if ( $kaigyo ) ;
		if ( $name ne $name_comment && $name ne 'msg' )	{	$value =~ s/\r\n//g;	$value =~ s/\r|\n//g;	}
		if ( ($tag ne 'yes' || $name ne $name_comment) &&  $name ne 'msg' )	{
			$value =~ s/&/&amp;/g;	$value =~ s/"/&quot;/g;
			$value =~ s/</&lt;/g;	$value =~ s/>/&gt;/g;
		}
		$value =~ s/\,/&#44;/g;
		$chkvalue = $value;$chkvalue2 = $value;
		foreach $dat( @errword )	{
			if ( $dat ne '' ) {
				$chk = $dat;
				&jcode'convert(*chk, "euc");
				#全角/半角カナ含まない？
				if ($chk !~ /[\xA1-\xFE][\xA1-\xFE]/) {		$dat =~ tr/a-z/A-Z/;}
				&jcode'convert(*chkvalue, "euc");
				if ($chkvalue !~ /[\xA1-\xFE][\xA1-\xFE]/) {	$chkvalue2 =~ tr/a-z/A-Z/;	}
				#検索文字列
				if ( index($chkvalue2,$dat) >= 0 ) {
					&error("投稿禁止単語が入力されていますので投稿出来ません");
				}
			}
		}
		if ( $urllink && ($name eq 'name' || $name eq 'hp' || $name eq 'msg' || $name eq $name_comment )) {
			if ( $urllink == 1 ) {
				if ( $value =~ /tp:\/\//i && $name ne 'hp' ) {
					&error("セキュリティ対策の為、URLは入力出来ません。");
				}
			}	else	{
				foreach $buf ( @urlerrnm ) {
					if ( $value =~ /([^=^\"]|^)(http|ftp)([\w|\!\#\&\=\-\%\@\~\;\+\:\.\?\/]+)/i ) {
						if ( $3 =~ /$buf/ ) {
							&error("文字「$buf」は、セキュリティ対策の為、入力出来ません。");
						}
					}
				}
			}
		}
		&jcode'convert(*value,'sjis');
		$FORM{$name} = $value;
	}
	if ( $FORM{'action'} eq 'regist' || $FORM{'action'} eq 'maintenance' ||
		 $FORM{'action'} eq 'update' || $FORM{'action'} eq 'update2' )	{
		if ( $postchk && !$post )	{	&error("不正な投稿です。");	}
		if ( $urlchk && $ENV{HTTP_REFERER} !~ /$urlchk/i )	{	exit;	}
	}
	$FORM{$name_comment} =~ s/\r\n/<br>/g;	$FORM{$name_comment} =~ s/\r|\n/<br>/g;
	$FORM{'hp'}   =~ s/^http\:\/\///;
	if ( $acs == 1 )	{	$FORM{'icon'} = $icon_imode ;	}
}
###<--------------------------------------------------------------
###<---   HTMLヘッダー書き出し
###<--------------------------------------------------------------
sub	header	{
	print "Content-type: text/html; charset=Shift_JIS\n";

if ( $env != 0 ){
	print "Pragma: no-cache\n";
	print "Cache-Control: no-cache\n";
	print "Expires: Thu, 01 Dec 1994 16:00:00 GMT\n";
}
print "\n";
if ( $env == 2 ) {
print <<"EOM";
<?xml version="1.0" encoding="Shift_JIS"?>
<!DOCTYPE html PUBLIC "-//OPENWAVE//DTD XHTML 1.0//EN"
http://www.openwave.com/DTD/xhtml-basic.dtd>
EOM
}
	print "<html>\n<head>\n";
	print "<META HTTP-EQUIV=\"Content-type\" CONTENT=\"text/html; charset=x-sjis\">\n";
	if ( $env != 0 ){
		print "<meta http-equiv=\"Pragma\" content=\"no-cache\">\n";	#ezweb対応
		print "<meta http-equiv=\"Cache-Control\" content=\"no-cache\">\n";
	}
	print "<title>$title</title>\n";
	#<<<CSS START>>>
	print "<style type=\"text/css\">\n";
	print "<!--\n";
	print "body,tr,td { font-size: $pt;}\n";
	if ( $scrollbar ) { print $scrollbar; }
	print "-->\n";
	print "</style>\n";
	#<<<CSS END>>>
	print "</head>\n";
	if ($backpicture) { $set = "background=\"$backpicture\""; if ( $bgcolor ) { $set .= " bgcolor=\"$bgcolor\"" ; }	}
	elsif ($bgcolor )	{ $set = "bgcolor=\"$bgcolor\""; }
	print "<body $set text=$textcolor link=$linkcolor vlink=$vlinkcolor alink=$alinkcolor>\n";
}
###<--------------------------------------------------------------
###<---   HTMLフッダー書き出し
###<--------------------------------------------------------------
sub footer {
	print "</body></html>\n";
}
###<--------------------------------------------------------------
###<---   ログファイル読み込み
###<--------------------------------------------------------------
sub	dataread	{
	#<<<ログ読み込み
	if ( !(open(IN,"$logfile")))	{	&error("ログファイル($logfile)のオープンに失敗しました");	}
	@LOG = <IN>;
	close(IN);
}
###<--------------------------------------------------------------
###<---   ヘッダー２
###<--------------------------------------------------------------
sub	header2	{
	if ( $acs == 0 )	{
		print "<table cellpadding=0 cellspacing=0 width=10%><tr>\n";
		print "<form>\n";
		if ( $url ) {
			print "<td><INPUT TYPE=button VALUE=\"HOME\" ";
			if ( $frame_home ) {
				print "onClick=\"parent.$frame_home.location.href = \'$url\'\" $css_style></td></form>\n";
			}	else	{
				print "onClick=\"parent.location.href = \'$url\'\" $css_style></td></form>\n";
			}
		}
		if ( $logfile2 && $FORM{'action'} ne 'download')	{	#i001112
			print "<form>\n";	#i000714
			print "<td width=5>&nbsp;</td><td><INPUT TYPE=button VALUE=\"ランキング\" ";
			if ( $frame_other ) {
				print "onClick=\"parent.$frame_other.location.href = \'$script?action=ranking\'\" $css_style></td></form>\n";
			}	else	{
				print "onClick=\"parent.location.href = \'$script?action=ranking\'\" $css_style></td></form>\n";
			}
		}
		if ( $logfile2 && $FORM{'action'} ne 'download')	{
			print "<form>\n";
			print "<td width=5>&nbsp;</td><td width=10%><INPUT TYPE=button VALUE=\"昇進資格説明\" ";
			if ( $frame_other ) {
				print "onClick=\"parent.$frame_other.location.href = \'$script?action=info\'\" $css_style></td></form>\n";
			}	else	{
				print "onClick=\"parent.location.href = \'$script?action=info\'\" $css_style></td></form>\n";
			}
		}
		print "</tr></table><br>\n";
		print "<center>" ;
	}	else	{
		if ( $url )	{	print "<a href=$url>[HOME]</a>";	}
		if ( $logfile2 && $FORM{'action'} ne 'download')	{	#i001112
			print "&nbsp;<a href=$script?action=ranking>[ランキング]</a>";
		}
		print "&nbsp;<a href=$script?action=input>[新規投稿]</a>" if ( $dsp_new == 1 ) ;
		print "<br><br>\n";
	}
	if ( $titlelogo )	{
		print "<img src=\"$titlelogo\"><br>\n";
	}	else	{
		print "$title<br>\n";
	}
}
###<--------------------------------------------------------------
###<---   入力フォーム
###<--------------------------------------------------------------
sub	inputform	{
	print "<form name=inputform action=$script method=$method>\n";
	if ( $FORM{'action'} ne 'maintenance' )	{
		print "<input type=hidden name=\"action\" value=\"regist\">\n";
	}	else	{
		print "<input type=hidden name=\"action\" value=\"update\">\n";
		print "<input type=hidden name=\"no\" value=\"$FORM{'no'}\">\n";
		print "<input type=hidden name=\"proc\" value=\"edit\">\n";
		print "<input type=hidden name=\"pass\" value=\"$FORM{'pass'}\">\n";
	}
#=================================================================
	if ( $acs == 0 )	{

	if ( $maru == 1 )	{
		print "<table border=0 cellspacing=0 cellpadding=0>\n";
		print "<tr>\n";
		print "<td bgcolor=\"$tbgcolor\"><img src=$top_l width=8 height=8></td>\n";
		print "<td bgcolor=\"$tbgcolor\"><img src=\"$gif_spacer\" width=1 height=1></td>\n";
		print "<td bgcolor=\"$tbgcolor\"><img src=$top_r width=8 height=8></td>\n";
		print "</tr>\n";
		print "<tr>\n";
		print "<td width=8 bgcolor=\"$tbgcolor\"><img src=\"$gif_spacer\" width=1 height=1></td>\n";
		print "<td bgcolor=\"$tbgcolor\" align=center>\n";
	}
	if ( $maru == 1 ) { $dmy = "width=100%"; } else { $dmy = ""; }
	if ( $maru == 0 ) { $dmy2 = 1; } else { $dmy2 = 0; }
	print "<table border=0 cellspacing=0 cellpadding=$dmy2 align=center $dmy>\n";
	if ( $maru == 0 ) { $bg = "bgcolor=#000000"; } else { $bg = "bgcolor=$tbgcolor"; }
	print "<tr><td align=center $bg>\n";
	if ( $maru == 0 ) {
		print "<table border=0 cellspacing=0 cellpadding=3 align=center width=100%>\n";
		print "<tr><td bgcolor=\"$tbgcolor\" align=center>\n";
	}
	$c_cm =~ s/&amp;/&/g;
	if ( $textflg != 1 )	{
		#■お名前
		print "&nbsp;&nbsp;Name</td>";
		print "<td bgcolor=\"$tbgcolor\"><input type=text name=\"name\" size=$name_sz value=\"$c_name\" $css_style></td>\n";
		print "<td bgcolor=\"$tbgcolor\" align=\"center\" rowspan=4>";
		print "<textarea name=\"$name_comment\" cols=$message_sz1 rows=$message_sz2 $css_style>$c_cm</textarea>&nbsp;&nbsp;<br>";
		if ( $passsw == 1 ) {
			print "パスワード<input type=\"password\" name=\"pass\" size=\"8\" value=\"$c_ps\" $css_style>&nbsp;&nbsp;\n";
		}
		print "<input type=submit value=$submit $css_style>";
		if ( $icon_flg eq 'yes' )	{	print "&nbsp;&nbsp;<a href=\"$script?action=icondisp\">アイコン一覧</a>";	}
		print "</td></tr>\n";
		#■アイコン
		if ( $icon_flg eq 'yes' )	{
			print "<tr><td bgcolor=\"$tbgcolor\">\n";
			print "&nbsp;&nbsp;Icon</td><td bgcolor=\"$tbgcolor\"><select name=\"icon\" value=$c_icon $css_style>\n";
			for ( $i = 0 ; $i <= $#iconnm ; $i++ ) {
				if ( $i == $c_icon )	{	$dmy = "selected";	}	else	{	$dmy = "" ;	}
				print "<option value=$i $dmy>$iconnm[$i]\n";
			}
			print "</select>&nbsp;&nbsp;</td></tr>\n";
		}
		if ( $emailflg == 1 ) {
			#■メールアドレス
			print "<tr><td bgcolor=\"$tbgcolor\">\n";
			print "&nbsp;&nbsp;Email</td><td bgcolor=\"$tbgcolor\"><input type=text name=\"email\" size=$email_sz value=\"$c_email\" $css_style>&nbsp;&nbsp;</td></tr>\n";
		}
		if ( $hpflg == 1 ) {
			#■Homepage
			print "<tr><td bgcolor=\"$tbgcolor\">\n";
			print "&nbsp;&nbsp;URL</td><td bgcolor=\"$tbgcolor\"><input type=text name=\"hp\" size=$hp_sz value=\"http://$c_hp\" $css_style>&nbsp;&nbsp;</td></tr>\n";
		}
		print "</table>\n";
	}	else	{
		print "<input type=text name=\"$name_comment\" size=$message_sz1 value=\"$c_cm\" $css_style>\n";
		print "<input type=submit value=$submit $css_style>";
		if ( $passsw == 1 ) {
			print "&nbsp;&nbsp;パスワード<input type=\"password\" name=\"pass\" size=\"8\" value=\"$c_ps\" $css_style>&nbsp;&nbsp;\n";
		}
		if ( $emailflg == 1 || $hpflg == 1 )	{
			if ( $icon_flg eq 'yes' )	{
				print "&nbsp;&nbsp;<a href=\"$script?action=icondisp\">アイコン一覧</a>&nbsp;&nbsp;\n";
			}
		}
		print "</td></tr><tr><td bgcolor=\"$tbgcolor\">\n";
		print "Name:";
		print "<input type=text name=\"name\" size=15 value=\"$c_name\" $css_style>\n";
		if ( $icon_flg eq 'yes' )	{
			print "&nbsp;Icon:<select name=\"icon\" value=$c_icon>\n";
			for ( $i = 0 ; $i <= $#iconnm ; $i++ ) {
				if ( $i == $c_icon )	{	$dmy = "selected";	}	else	{	$dmy = "" ;	}
				print "<option value=$i $dmy>$iconnm[$i]\n";
			}
			print "</select>\n";
		}
		if ( $emailflg == 0 && $hpflg == 0 )	{
			if ( $icon_flg eq 'yes' )	{
				print "&nbsp;&nbsp;<a href=\"$script?action=icondisp\">アイコン一覧</a>\n";
			}
			print "</td></tr>\n";
		}	else	{
			if ( $emailflg == 1 ) {
				print "&nbsp;Email:<input type=text name=\"email\" size=15 value=\"$c_email\" $css_style>\n";
			}
			if ( $hpflg == 1 ) {
				print "&nbsp;URL:<input type=text name=\"hp\" size=15 value=\"http://$c_hp\" $css_style>\n";
			}
			print "</td></tr>\n";
		}
		print "</table>\n";
	}
	if ( $maru == 0 ) {
		print "</td></tr></table>\n";
	}
	if ( $maru == 1 )	{
		print "</td>\n";
		print "<td width=8 bgcolor=\"$tbgcolor\"><img src=\"$gif_spacer\" width=1 height=1></td>\n";
		print "</tr>\n";
		print "<tr>\n";
		print "<td bgcolor=\"$tbgcolor\"><img src=$bottom_l width=8 height=8></td>\n";
		print "<td bgcolor=\"$tbgcolor\"><img src=\"$gif_spacer\" width=1 height=1></td>\n";
		print "<td bgcolor=\"$tbgcolor\"><img src=$bottom_r width=8 height=8></td>\n";
		print "</tr>\n";
		print "</table>\n";
	}

	}	else	{		#imode時
		#■お名前
		print "■Name<br>";
		print "<input type=text name=\"name\" size=$name_sz value=\"$c_name\"><br>\n";
		if ( $emailflg == 1 ) {
			#■メールアドレス
			print "■Email<br><input type=text name=\"email\" size=$email_sz value=\"$c_email\"><br>\n";
		}
		if ( $hpflg == 1 ) {
			#■Homepage
			print "■URL<br><input type=text name=\"hp\" size=$hp_sz value=\"http://$c_hp\"><br>\n";
		}
		print "■Message<br>";
		if ( $textflg != 1 )	{
			print "<textarea name=\"$name_comment\" cols=$message_sz1 rows=$message_sz2 $css_style>$c_cm</textarea><br>";
		}	else	{
			print "<input type=text name=\"$name_comment\" size=$message_sz1 value=\"$c_cm\">\n";
		}
		print "<br><input type=submit value=$submit>";
	}
	print "</form>";

	if ( $manual == 1 )	{	&setumei;	}	#<<<「使い方」の表示

	print "</center>\n" if ( $acs == 0 ) ;
	if ( $acs == 0 )	{
		print "<SCRIPT Language=JavaScript>\n";
		print "<!--\n";
		if ( $c_name eq "" ) 	{
			print "document.inputform.name.focus();\n";
		}	else	{
			print "document.inputform.$name_comment.focus();\n";
		}
		print "// -->\n";
		print "</SCRIPT>\n";
	}
}
###<--------------------------------------------------------------
###<---   みなさんからの挨拶を表示
###<--------------------------------------------------------------
sub	disp	{

	if ( $acs == 0 )	{
		print "<center>\n";
		print "<br><font size=+2>$title</font><br><br>\n" if ( $FORM{'action'} eq 'download' ) ;;
		if ( !(open(IN3,"$logfile3")))	{	&error("ログファイル３($logfile3)のオープンに失敗しました");	}
		@message = <IN3>;
		close(IN3);
		foreach ( @message ) {
			($n,$m) = split(/:/,$_);
			if ( $c_name eq $n )	{
				print "<br><b>$m</b><hr width=80% size=1>\n";
			}
		}
		print "<br><table border=0 cellspacing=0 cellpadding=0 width=$tsz bgcolor=#000000><tr><td>\n";
		print "<table border=0 cellspacing=1 cellpadding=3 width=100%>\n";
		print "<tr><td bgcolor=$cellheadbgcolor align=right><font color=#000000>No</font></td>\n";
		print "<td bgcolor=$cellheadbgcolor><font color=#000000>Date</font></td>\n";
		print "<td bgcolor=$cellheadbgcolor width=70><font color=#000000>Name</font></td>\n";
		if ( $icon_flg eq 'yes' && $FORM{'action'} ne 'download' )	{
			print "<td bgcolor=$cellheadbgcolor align=\"center\" width=50><font color=#000000>Icon</font></td>\n";
		}
		if ( $hpflg == 1 )	{	print "<td bgcolor=$cellheadbgcolor align=\"center\" width=50><font color=#000000>URL</font></td>\n";	}
		print "<td bgcolor=$cellheadbgcolor width=40%><font color=#000000>Message</font></td>\n";
		if ( $logfile2 )	{
			print "<td bgcolor=$cellheadbgcolor nowrap align=center><font color=#000000>回数</font></td>";
			print "<td bgcolor=$cellheadbgcolor nowrap width=10% align=center><font color=#000000>昇進状態</font></td>";
		}
		print "</tr>\n";
	}	else	{
		if ( !(open(IN3,"$logfile3")))	{	&error("ログファイル３($logfile3)のオープンに失敗しました");	}
		@message = <IN3>;
		close(IN3);
		foreach ( @message ) {
			($n,$m) = split(/:/,$_);
			if ( $c_name eq $n )	{
				print "▼MESSAGE<br><b>$m</b>\n";
			}
		}
	}
	if ( !(open(IN,"$logfile")))	{	&error("ログファイル($logfile)のオープンに失敗しました");	}
	@data = <IN>;	close(IN);

	#表示対象ページの先頭データ件数を算出
	$dm = @data;
	if ( $dm % $pagemax == 0) {		$p = $dm / $pagemax ;
	}	else	{		$p = $dm / $pagemax + 1;	}
	$p = sprintf("%3d",$p);
	if ( $FORM{'page'} eq "NEXT" )	{
		if ( $FORM{'disppage'} == 0 ) { $FORM{'disppage'} = 1 }	;
		$d = ($FORM{'disppage'} + 1) * $pagemax - $pagemax ;
		$FORM{'disppage'} = $FORM{'disppage'} + 1 ;
	}	elsif	( $FORM{'page'} eq "BACK" ) 	{
		$d = ($FORM{'disppage'} - 1) * $pagemax - $pagemax ;
		$FORM{'disppage'} = $FORM{'disppage'} - 1 ;
	}	else	{
		$d = 0	;
		$FORM{'disppage'} = 1 ;
	}
	$z = 1 ;
	if ( $FORM{'action'} eq 'download' ) { #i001112
		$d = 0 ; $pagemax = $dm ;	$icon_flg = "no";
	}
	for ( $i = $d ; ( $z <= $pagemax ) && ( $i < $dm ); $i++ )	{
		($no,$dt,$nm,$cm,$cnt,$icon,$email,$hp,$hst,$dmy) = split(/,/,$data[$i]);
		($svdate,$svtime) = split(/ /,$dt);
		$raihoucnt = sprintf("%d",$cnt);
		$edt = substr($svdate,4,2);		$edt = sprintf("%02d",$edt)."/";
		$edt2 = substr($svdate,6,2);		$edt = $edt.sprintf("%02d",$edt2);
		if ( $acs == 0 )	{
			if ( $bg eq $cellbgcolor1 ) {			$bg = $cellbgcolor2;
			}	else	{			$bg = $cellbgcolor1;		}
			print "<tr><td bgcolor=$bg nowrap width=10 align=right><font color=$textcolor>$no</font></td>\n";
			if ( $cm ne 'OIWAI' )	{
				print "<td bgcolor=$bg  width=1% nowrap><font color=$textcolor>$edt-$svtime</font></td>\n";
				print "<td bgcolor=$bg width=70>";
				if ( $email ) {
					print "<a href=\"mailto:$email\">$nm</a>\n";
				}	else	{
					print "<font color=$textcolor>$nm</font>";
				}
				print "</td>\n";
				if ( $icon_flg eq 'yes' )	{
					print "<td bgcolor=$bg align=\"center\" width=1% nowrap>\n";
					&icon_set($nm) ;
					print "</td>\n";
				}
				if ( $hpflg == 1 )	{
					print "<td bgcolor=$bg align=\"center\" width=1% nowrap>";
					if ( $hp )	{	print "<a href=\"http://$hp\" target=_top>[URL]</a></td>\n";	}
					else	{	print "&nbsp;</td>\n";	}
				}
				if ( $cm eq '' ) {	$cm = '　';	}
				$cm =~ s/&amp;/&/g;
				print "<td bgcolor=$bg ><font color=$textcolor>$cm";
				print " ...($hst)" if ( $host_disp == 1 ) ;
				print "</font></td>\n";
				if ( $logfile2 )	{	#i001112
					print "<td bgcolor=$bg align=right width=60><font color=$textcolor>$raihoucnt回</font></td>\n";
					$ranking = &rankget($raihoucnt) ;
					print "<td bgcolor=$bg align=center nowrap><font color=$textcolor>\n";
					print "<img src=$rankicon[$ranking]>\n" if ( $rankicon[$ranking] ) ;
					print "$rank[$ranking]\n" if ( !($rankicon[$ranking]) ) ;
					print "</font></td>\n";
				}
				print "</tr>\n";
			}	else	{
				$cs = 7 ;
				if ( $icon_flg ne 'yes' )	{	$cs--;	}
				if ( $hpflg != 1 )	{	$cs--;	}
				if ( $logfile2 eq '' )	{	$cs--;	}
				print "<td bgcolor=$oiwaibgcolor colspan=$cs>\n";
				$wk = $oiwaimsg ;
				$wk =~ s/NAME/$nm/i;	$wk =~ s/CNT/$raihoucnt/i;
				print "<font color=$oiwaitxcolor>$wk</font>";
				print "</td></tr>";
			}
		}	else	{
			print "<hr>";
			print "[$no]..$edt-$svtime<br>\n";
			if ( $email ) {
				print "<a href=\"mailto:$email\">$nm</a>\n";
			}	else	{
				print "$nm";
			}
			if ( $logfile2 )	{	#i001112
				$ranking = &rankget($raihoucnt) ;
				print "($raihoucnt回…$rank[$ranking])\n";
			}
			if ( $hpflg == 1 )	{
				if ( $hp )	{	print "<a href=\"http://$hp\" target=_top>-[URL]</a>\n";	}
			}
			print "<br>\n";
			if ($cm ne "OIWAI") {
				$wk = "$cm";
			} else {
				$wk = $oiwaimsg_i;
				$wk =~ s/NAME/$nm/i; $wk =~ s/CNT/$raihoucnt/i;
				$wk = "<font color=$oiwaitxcolor_i>$wk</font>";
			}
			print "$wk\n";
		}
		$z++;
	}
	print "</table></td></tr></table>\n" if ( $acs == 0 );
	if ( $FORM{'action'} ne 'download' )	{	#i001112
		print "<form action=$script method=$method>\n";
		print "<input type=hidden name=\"disppage\" value=$FORM{'disppage'}>\n";
		if ( $FORM{'disppage'} != 0 && $FORM{'disppage'} !=1)	{
			print "<input type=submit name=\"page\" value=BACK>\n";
		}
		if ( $FORM{'disppage'} + 1 <= $p )	{
			print "<input type=submit name=\"page\" value=NEXT>\n";
		}
		print "</form>\n";
	}
	if ( $acs == 0 )	{
		if ( $logfile2 )	{	#i001112
			print "<br>TotalCountは、あなたの過去からの挨拶回数です♪</font><br><br>";
		}
	}	else	{
		print "( )の数字は投稿回数です\n";
	}
	if ( $acs == 0 )	{	#i001112
		print "<hr size=1 noshade color=#000000>\n" ;
		print "<form action=\"$script\" method=\"$method\">\n";
		print "<input type=hidden name=\"action\" value=\"download\">\n";
		print "<input type=submit value=\"ログをダウンロード\" $css_style>\n";
		print "<br>拡張子はhtmに変更して下さい";
		print "</form>\n";
	}
}
###<--------------------------------------------------------------
###<---   挨拶ログ出力
###<--------------------------------------------------------------
sub	regist	{
	if ( $FORM{'name'} eq "")	{	&error("名前は省略出来ません。") ;	}
	if ( $maxword ne '' && (length($FORM{$name_comment}) > $maxword))	{	&error("メッセージは$maxword文字までしか登録出来ません。");	}
	if ( $textflg2 == 1 && $FORM{$name_comment} eq '' )	{	&error("メッセージ欄は省略出来ません。") ;	}
	if ( $mailerr == 1 && $FORM{'email'} ) { &error("セキュリティ対策の為、メールアドレスは入力出来ません。");	}
	if ( $urlerr == 1 && $FORM{'hp'} ) { &error("セキュリティ対策の為、URLは入力出来ません。");	}
	# URLと同じものが本文にあったら宣伝
	if ($FORM{'hp'}){
		if ( $FORM{$name_comment} =~ /$FORM{'hp'}/) {
			&error("宣伝投稿と見なされますので投稿出来ません");
		}
	}
	if ( $urlcnt ) {
		$urlnum = ($FORM{$name_comment} =~ s/(h?ttp)/$1/ig);
		if ( $urlnum > $urlcnt ) { &error("URLは" . ($urlcnt + 1) . "個以上は記入出来ません"); }
	}
	if ( $japan ) {
		$str = $FORM{$name_comment};
		jcode::convert(\$str, 'euc','sjis');
		if($str =~ /[\xA1-\xFE][\xA1-\xFE]/ || $str =~ /\x8E/ || $str =~ /[\x8E\xA1-\xFE]/){
		}	else	{
			&error("半角英数字のみの投稿は出来ません。");
		}
	}

	# ホスト名を取得
	$host  = $ENV{'REMOTE_HOST'};	$addr  = $ENV{'REMOTE_ADDR'};
	if ($host eq "" || $host eq "$addr") {
		($p1,$p2,$p3,$p4) = split(/\./,$addr);
		$temp = pack("C4",$p1,$p2,$p3,$p4);
		$host = gethostbyaddr("$temp", 2);
		if ($host eq "") { $host = $addr; }
	}
	#掲示板荒らし対策
	foreach $buf(@DANGER_LIST){
		if ( $buf ) {
			# パターンマッチを変換
			$buf=~ s/\./\\./g;		$buf=~ s/\?/\./g;		$buf=~ s/\*/\.\*/g;
			if($host =~ /$buf/gi){	&error("\申\し\訳ありません。<br>あなたのプロバイダーからは投稿できませんでした． ");	}
		}
	}
	&filelock ;		#ファイルロック
	&dataread ;
	$dcnt2 = @LOG;
	if ($dcnt2 >= $datamax) {	pop(@LOG);	}
	if ( $dcnt2 < 1 )	{
		$no = 1;										#１件目
	}	else	{
		($no,$dt,$nm,$cm,$cnt,$icon,$email,$hp,$hst,$dmy) = split(/,/,$LOG[0]);
		$no++ ;
	}
	if ( $renchan1 != 0 || $renchan2 != 0 )	{
		$write_cnt = 1 ;
		foreach $buf ( @LOG )	{
			($n,$dt,$nm,$cm,$cnt,$icon,$email,$hp,$hst,$dmy) = split(/,/,$buf);
			if ( $renchan2 != 0 && $cm ne 'OIWAI' && $hst eq $host )	{
				$write_cnt++ ;
				if ( $write_cnt >= $renchan2 )	{	&fileunlock ;	&error("$renchan2回以上の連続投稿は禁止しています");	}
			}
			if ( $renchan2 != 0 && $hst ne $host )	{	last ; }	#i001220
			if ( $renchan1 != 0 && $dt ge $renday )	{
				if ( $hst eq $host )	{	&fileunlock ;	&error("$renchan1分以内の連続投稿は禁止しています");	}
			}
		}
	}
	if ( $logfile2 )	{
		if ( !(open(IN2,"$logfile2")))	{	&fileunlock ;	&error("ログファイル２($logfile2)のオープンに失敗しました");	}
		@sv = ();
		$flg = 0 ;
		while ( <IN2> )	{
	 		($n,$k) = split(/,/,$_);
			$k =~ s/\n//;
			if ( $FORM{'name'} eq $n )	{
				$k++;	$dcnt = $k ;	$flg = 9;
			}
			$k = sprintf("%03d",$k);
			push(@sv,"$n,$k\n");
		}
		if ( $flg == 0 ) 	{
			push(@sv,"$FORM{'name'},001\n");
			$dcnt = 1;
		}
		close(IN2);
		if ( !(open(OUT,">$logfile2")))	{	&fileunlock ;	&error("ログファイル($logfile)のオープンに失敗しました");	}
		print OUT @sv;
		close(OUT);
	}
	# パスワードの暗号化（crypt関数使用））
	if ($FORM{'pass'} ne "") { &pass_enc($FORM{'pass'}); }	else	{ $pass = '' ; }
	unshift(@LOG,"$no,$today,$FORM{'name'},$FORM{$name_comment},$dcnt,$FORM{'icon'},$FORM{'email'},$FORM{'hp'},$host,$pass\n");

	foreach $buf ( @OIWAI )	{
		if ( $dcnt == $buf )	{
			$dcnt2 = @LOG;
			if ($dcnt2 >= $datamax) {	pop(@LOG);	}
			$no++ ;
			unshift(@LOG,"$no,$today,$FORM{'name'},OIWAI,$dcnt,,$FORM{'email'},,$host,$pass\n");
			last ;
		}
	}

	if ( !(open(OUT,">$logfile")))	{	&fileunlock ;	&error("ログファイル($logfile)のオープンに失敗しました");	}
	print OUT @LOG;
	close(OUT);
	&fileunlock ;	#ファイルロック解除

	#COOKIE設定
	&cookieset ;
}
###<--------------------------------------------------------------
###<---   使い方の説明部分
###<--------------------------------------------------------------
sub setumei	{
	print "<hr size=1 noshade color=#000000><br>\n";
	#使い方を表示する
	if ( $acs == 0 ) {	print $manualmsg;	}
	else	{ print $manualmsg2;	}
}
###<-------------------------------------------------------------
###<---   クッキー取得
###<--------------------------------------------------------------
sub cookieget	{
	$cookies = $ENV{'HTTP_COOKIE'};
	@pairs = split(/;/,$cookies);
	foreach $pair (@pairs) {
		($name, $value) = split(/=/, $pair);
		$name =~ s/ //g;
		$DUMMY{$name} = $value;
	}
	@pairs = split(/,/,$DUMMY{'sicharou'});
	foreach $pair (@pairs) {
		($name, $value) = split(/\!/, $pair);
		$value =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack("C",hex($1))/eg;
		$value =~ s/\+/ /g;
		$COOKIE{$name} = $value;
	}
	if ( $env != 0 && $FORM{'action'} eq 'regist') {
		$c_name  = $FORM{'name'};
		$c_icon  = $FORM{'icon'};
		$c_email  = $FORM{'email'};
		$c_hp  = $FORM{'hp'};
	}	else	{
		$c_name  = $COOKIE{'nm'};
		$c_icon  = $COOKIE{'icon'};
		$c_email  = $COOKIE{'em'};
		$c_hp  = $COOKIE{'hp'};
	}
}
###<-------------------------------------------------------------
###<---   クッキー設定
###<--------------------------------------------------------------
sub cookieset {
	($secg,$ming,$hourg,$mdayg,$mong,$yearg,$wdayg,$ydayg,$isdstg)
		=gmtime(time + 30*24*60*60);
	$yearg  += 1900 ;
	if ($secg  < 10)  { $secg  = "0$secg";  }
	if ($ming  < 10)  { $ming  = "0$ming";  }
	if ($hourg < 10)  { $hourg = "0$hourg"; }
	if ($mdayg < 10)  { $mdayg = "0$mdayg"; }
	$mong = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')[$mong];
	$youbi = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')[$wdayg];
	$date_gmt = "$youbi, $mdayg\-$mong\-$yearg $hourg:$ming:$secg GMT";
#	$FORM{'name'} =~ s/(\W)/sprintf("%%%02X", unpack("C", $1))/eg;
#	$FORM{'hp'} =~ s/(\W)/sprintf("%%%02X", unpack("C", $1))/eg;
	$cook="nm\!$FORM{'name'},icon\!$FORM{'icon'},em\!$FORM{'email'},hp\!$FORM{'hp'},ps\!$FORM{'pass'}";
	print "Set-Cookie: sicharou=$cook; expires=$date_gmt\n";
}
###<--------------------------------------------------------------
###<---   メンテナンスモード
###<--------------------------------------------------------------
sub Maintenance {
	if ( $FORM{'proc'} ne 'message' && $FORM{'no'} eq "")	{	&error("メンテナンス対象の記事Noを指定して下さい。");	}
	if ( $FORM{'pass'} eq "")	{	&error("パスワードを入力して下さい。");	}

	#投稿ログのメンテナンス
	if ( $FORM{'proc'} eq 'edit' )	{
		&logmtn;
	}
	#投稿ログの削除
	if ( $FORM{'proc'} eq 'delete' )	{
		&update;
	}
	#訪問者用メッセージのメンテナンス
	if ( $FORM{'proc'} eq 'message' )	{
		&msgmtn;
	}
}
###<--------------------------------------------------------------
###<---   ログファイル・メンテナンス
###<--------------------------------------------------------------
sub logmtn {
	if ( $FORM{'no'} eq "")		{	&error("記事Noを入力して下さい。");	}
	if ( $FORM{'pass'} eq "")	{	&error("パスワードを入力して下さい。");	}

	$found = 0 ;
	&dataread ;																#<<<ログ読み込み
	foreach ( @LOG )	{
		($no,$dt,$nm,$cm,$cnt,$icon,$email,$hp,$hst,$ps) = split(/,/,$_);
		if ( $FORM{'no'} eq $no )	{
			$ps =~ s/\n//;
			if ($FORM{'pass'} ne $password && (&pass_dec($ps))) { &error("パスワードが違います。"); }
			$found = 1 ;
			if ( $FORM{'proc'} eq "delete" )	{
				&update ;
				exit;
			}
			if ( $cm eq 'OIWAI' ) {&error("昇進メッセージデータは修正出来ません。"); }
			&header ;
			$c_name = $nm ;	$c_icon = $icon ;	$c_email = $email ;	$c_hp = $hp ;
			$c_ps = $ps; $c_cm = $cm; $c_cm =~ s/<br>/\n/gi;
			$c_ps = $FORM{'pass'};
			&inputform ;
			last;
		}
	}
	if ( $found == 0 )	{
		&error("該当する記事Noのデータは存在していません。");
	}
	&footer ;
	exit;

}
###<--------------------------------------------------------------
###<---   来訪者用メッセージファイル・メンテナンス
###<--------------------------------------------------------------
sub msgmtn {

	if ( !(open(IN,"$logfile3")))	{	&error("ログファイル３($logfile3)のオープンに失敗しました");	}
	@data = <IN>;	close(IN);

	&header ;
	print "<a href=$script>[BACK]</a>\n";
if ( $acs == 0 )	{
	print "<center>\n";
print <<"EOM";
<table cellpadding=7><tr><td bgcolor=#990000><font color=#ffffff>
<pre>
■来訪者毎に特定のメッセージを表\示する設定を行います■

来訪者がクッキーを許可している場合、ここで登録した名前の人がアクセスした
際に設定したメッセージが表\示されます
<hr>
設定方法は、「訪問者の名前」+「:（半角コロン）」＋「表\示メッセージ」＋「改行」で
お一人様のメッセージとなります。
文章の途中で改行した場合はメッセージに&lt;br&gt;を入れて設定して下さい。<br>
　例：
　　Ａさん:いつも来てくれてありがとう
　　Ｂさん:しばらく来てないねぇ・・・
　　Ｃさん:Ｃさんへ！&lt;br&gt;&lt;b&gt;誕生日おめでとー!!!&lt;/b&gt;
　　※タグを挿入可能\です。
</td></tr></table>
EOM
}	else	{
print <<"EOM";
<br>■来訪者毎のメッセージ設定■<br>
<hr>
「訪問者の名前」+「:（半角コロン）」＋「表\示メッセージ」＋「改行」で
お一人様のメッセージとなります。
文章の途中で改行した場合はメッセージに&lt;br&gt;を入れて設定して下さい。<br>
EOM
}
	foreach ( @data )	{
		($nm,$cm) = split(/:/,$_);
		$cm =~ s/\n//;
		if ($nm eq '' || $cm eq '') { next; } #i001215
		$BUF .= "$nm:$cm\r";
	}
	print "<form action=$script method=$method>\n";
	print "<input type=\"hidden\" name=\"action\" value=\"update2\">\n";
	if ( $acs == 0 )	{
		print "<textarea name=\"msg\" cols=70 rows=10>$BUF</textarea>\n";
		print "<br><input type=submit value=訪問者メッセージを更新する>\n";
		print "</form></center>\n";
	}	else	{
		print "<textarea name=\"msg\" cols=$message_sz1 rows=$message_sz2 >$BUF</textarea>\n";
		print "<br><input type=submit value=更新>\n";
		print "</form>\n";
	}
	&footer ;
	exit ;
}
###<--------------------------------------------------------------
###<---   ログファイル更新
###<--------------------------------------------------------------
sub update {

	@DELWORD = split(/ /,$FORM{'no'});

	&filelock ;		#ファイルロック
	&dataread ;
    foreach (@LOG) {
		($no,$dt,$nm,$cm,$cnt,$icon,$email,$hp,$hst,$ps) = split(/,/,$_);
        if ($FORM{'no'} eq $no ) {									#<<<編集対象データの場合
			$ps =~ s/\n//;
			if ($FORM{'pass'} ne $password && (&pass_dec($ps))) {
				&fileunlock ;	#ファイルロック解除
				&error("パスワードが違います。");
			}
			if ( $FORM{'proc'} ne 'delete' )	{
				push(@new,"$no,$dt,$FORM{'name'},$FORM{$name_comment},$cnt,$FORM{'icon'},$FORM{'email'},$FORM{'hp'},$hst,$ps\n");			#編集後の内容で置換
			}	else	{
				if ( $logfile2 )	{
					if ( !(open(IN2,"$logfile2")))	{	&fileunlock ;	&error("ログファイル２($logfile2)のオープンに失敗しました");	}
					@sv = ();
					$flg = 0 ;
					while ( <IN2> )	{
				 		($n,$k) = split(/,/,$_);
						$k =~ s/\n//;
						if ( $nm eq $n )	{	$k--;	}
						$k = sprintf("%03d",$k);
						push(@sv,"$n,$k\n");
					}
					close(IN2);
					if ( !(open(OUT,">$logfile2")))	{	&fileunlock ;	&error("ログファイル($logfile)のオープンに失敗しました");	}
					print OUT @sv;
					close(OUT);
				}
			}
		}	else	{										#<<<編集対象データ以外の場合
			$found = 0 ;
			if ( $FORM{'proc'} eq 'delete' ) {
				foreach $word ( @DELWORD )	{
					if ( $word && ( $no == $word ) ) {
						if ( $logfile2 )	{
							if ( !(open(IN2,"$logfile2")))	{	&fileunlock ;	&error("ログファイル２($logfile2)のオープンに失敗しました");	}
							@sv = ();
							$flg = 0 ;
							while ( <IN2> )	{
						 		($n,$k) = split(/,/,$_);
								$k =~ s/\n//;
								if ( $nm eq $n )	{	$k--;	}
								$k = sprintf("%03d",$k);
								push(@sv,"$n,$k\n");
							}
							close(IN2);
							if ( !(open(OUT,">$logfile2")))	{	&fileunlock ;	&error("ログファイル($logfile)のオープンに失敗しました");	}
							print OUT @sv;
							close(OUT);
						}
						$found = 1 ; last ;
					}
				}
			}
			if ( $found == 0 ) { push(@new,$_);	}
		}
	}
	if ( !(open(OUT,">$logfile")))	{	&fileunlock ;	&error("ログファイル($logfile)のオープンに失敗しました");	}
	print OUT @new;
	close(OUT);

	&fileunlock ;	#ファイルロック解除
	if ( $damedame == 0 )	{
		print "Location: $script?\n\n";
	}	else	{
		print "Content-type: text/html\n\n";
		print "<html><head><META HTTP-EQUIV=\"Refresh\" CONTENT=\"0; URL=";
		print "$script?\">";
		print $dmy_tok2_cookie; # クッキーの発効
		print "</head><body></body></html>\n\n";
	}

}
###<--------------------------------------------------------------
###<---   来訪者用メッセージファイル更新
###<--------------------------------------------------------------
sub update2 {
	&filelock ;		#ファイルロック
	@MSGTBL = split(/\r/,$FORM{'msg'});
	foreach $buf ( @MSGTBL )	{	if ( $buf )	{	push(@MSGTBL2,$buf) ;	}	}
	if ( !(open(OUT,">$logfile3")))	{	&fileunlock ;	&error("ログファイル($logfile)のオープンに失敗しました");	}
	print OUT @MSGTBL2;
	close(OUT);

	&fileunlock ;	#ファイルロック解除
	if ( $damedame == 0 )	{
		print "Location: $script?\n\n";
	}	else	{
		print "Content-type: text/html\n\n";
		print "<html><head><META HTTP-EQUIV=\"Refresh\" CONTENT=\"0; URL=";
		print "$script?\">";
		print $dmy_tok2_cookie; # クッキーの発効
		print "</head><body></body></html>\n\n";
	}

}
###<--------------------------------------------------------------
###<---   ランキング表示
###<--------------------------------------------------------------
sub ranking {
	if ( !(open(IN,"$logfile2")))	{	&error("ログファイル２($logfile2)のオープンに失敗しました");	}
	@data = <IN>;
	close(IN);

	$totalcount = @data ;

	&header ;
	print "<a href=$script>戻る</a><br>\n";

	@Lank = ();
    foreach $buf (@data) {
		($a,$b) = split(/,/,$buf);
		push(@Lank,"$b,$a");
	}
	@Lank = sort { $a <=> $b } @Lank ;
	@Lank = reverse @Lank ;
	print "<center>" if ( $acs == 0 ) ;
	print "<<<<< ランキング >>>>><br><br>\n";
	$c = $totalcount - 1;
	print "総投稿者数==>$c人<br>\n";
	if ( $acs == 0 )	{
		print "<table border=0 width=50% cellspacing=3 cellpadding=5>\n";
		print "<td bgcolor=$cellheadbgcolor width=3% nowrap><font color=#ffffff>ランキング</font></td>\n";
		print "<td bgcolor=$cellheadbgcolor width=70%><font color=#ffffff>お名前</font></td>\n";
		print "<td bgcolor=$cellheadbgcolor nowrap><font color=#ffffff>投稿回数</font></td>\n";
		print "<td bgcolor=$cellheadbgcolor width=2% nowrap>&nbsp;</td></tr>\n";
	}
	$cnt=1;
	foreach $buf ( @Lank )	{
		($raihoucnt,$nm) = split(/,/,$buf);
		if ( $nm ne $kanriname)	{
			if ( $bg eq $cellbgcolor1 ) {
				$bg = $cellbgcolor2;
			}	else	{
				$bg = $cellbgcolor1;
			}
			$raihoucnt = sprintf("%d",$raihoucnt);
			for ( $j = 0 ; $j <= $#OIWAI ; $j++ )	{
				if ( $raihoucnt >= $OIWAI[$j] )	{
					$ranking = $j ;
				}
			}
			if ( $acs == 0 )	{
				print "<tr><td bgcolor=$bg><font color=$textcolor>■$cnt位</font></td>\n";
				print "<td bgcolor=$bg><font color=$textcolor>$nm</font></td>\n";
				print "<td bgcolor=$bg align=right><font color=$textcolor>$raihoucnt回</font></td>\n";
				print "<td bgcolor=$bg nowrap align=right><img src=\"$rankicon[$ranking]\"></td>\n" if ( $rankicon[$ranking] ) ;
				print "<td bgcolor=$bg width=2% nowrap align=right><font color=$textcolor>$rank[$ranking]</font></td>\n" if ( !($rankicon[$ranking]) ) ;
				print "</tr>\n";
			}	else	{
				print "■$cnt位：$nm($raihoucnt回…$rank[$ranking])<br>";
			}
			$cnt++ ;
		}
		if ( $cnt > $rankcnt ) {	last ;	}
	}
	if ( $acs == 0 ) {
		print "</table><br><br>\n";
		print "</center>" ;
		&footer ;
	}	else	{
		print "</body></html>\n";
	}
}
###<--------------------------------------------------------------
###<---   Information(アイコン一覧)
###<--------------------------------------------------------------
sub icondisp	{
	&header ;															#<<<htmlヘッダー出力
	print "<center><br><br>■■■ アイコン一覧 ■■■<br><br>\n";
	print "<table cellpadding=5 cellspacing=0 border=0>\n";
	$i = 0 ; $j = 0 ;
	while ( 1 )	{
		print "<tr>\n";
		for ( $ln = 1 ; $j <= $#icon_gif && $ln <= $icon_line ; ) {
			print "<td align=\"center\"><img src=\"$icon_gif[$j]\" border=0></td>\n";
			print "<td align=\"center\">$iconnm[$j]</td>\n";
			$j++ ; $ln++ ;
		}
		if ( $j > $#icon_gif ) {
			if ( $ln < $icon_line ) {
				for ( ; $ln <= $icon_line ; ) {
					print "<td align=\"center\">&nbsp;</td>\n";
					print "<td align=\"center\">&nbsp;</td>\n";
					$ln++ ;
				}
			}
			print "</tr>\n";
			last ;
		}
		print "</tr>\n";
		$i++;
	}
	print "</table>";
	if ( $jiconnm[0] ne '' )	{
		print "<hr width=80% size=1>\n";
		print "<br>▼常連様専用のアイコンです▼<br><table cellpadding=5 cellspacing=0 border=0>\n";
		$i = 0 ; $j = 0 ;
		while ( 1 )	{
			print "<tr>\n";
			for ( $ln = 1 ; $j <= $#jicon_gif && $ln <= $icon_line ; ) {
				print "<td align=\"center\"><img src=\"$jicon_gif[$j]\" border=0></td>\n";
				print "<td align=\"center\">$jiconnm[$j]</td>\n";
				$j++ ; $ln++ ;
			}
			if ( $j > $#jicon_gif ) {
				if ( $ln < $icon_line ) {
					for ( ; $ln <= $icon_line ; ) {
						print "<td align=\"center\">&nbsp;</td>\n";
						print "<td align=\"center\">&nbsp;</td>\n";
						$ln++ ;
					}
				}
				print "</tr>\n";
				last ;
			}
			print "</tr>\n";
			$i++;
		}
		print "</table>";
	}
	print "</center>\n";
	&footer ;															#<<<htmlフッター出力
	exit;
}
###<--------------------------------------------------------------
###<---   エラー処理
###<--------------------------------------------------------------
sub error {
	&header ;
	print "<font  color=\"$textcolor\">$_[0]</font>\n";
	&footer;
	exit;
}
###<--------------------------------------------------------------
###<---   ファイルロック設定
###<--------------------------------------------------------------
sub filelock {
	foreach (1 .. 5) {
		if (-e $lockfile) { sleep(1); }
		else {
			open(LOCK,">$lockfile");
			close(LOCK);
			return;
		}
	}
	&error("只今他の方が書き込み中です。ブラウザの「戻る」で戻って再度登録を行って下さい。");
}
###<--------------------------------------------------------------
###<---   ファイルロック解除
###<--------------------------------------------------------------
sub fileunlock {
	if (-e $lockfile) { unlink($lockfile); }
}
###<--------------------------------------------------------------
###<---   アイコン表示
###<--------------------------------------------------------------
sub icon_set	{
	#常連者の投稿の場合、常連者用アイコンに置き換える
	$found = 0 ;
	for ( $k = 0 ; $k <= $#jiconnm ; $k++ )	{
		if ( $_[0] eq $jiconnm[$k] )	{
			$found = 1 ;
			if ( $jicon_gif_w[$k] != 0 ) { $dmy = "width=\"$jicon_gif_w[$k]\" height=\"$jicon_gif_h[$k]\"" ; } else { $dmy = "" ; }
			print "<img src=\"$jicon_gif[$k]\" $dmy border=0>";
			last ;
		}
	}
	if ( $found == 0 )	{
		if ( $_[0] eq $oiconnm )	{
			$found = 1 ;
			if ( $oicon_gif_w != 0 ) { $dmy = "width=\"$oicon_gif_w\" height=\"$oicon_gif_h\"" ; } else { $dmy = "" ; }
			print "<img src=\"$oicon_gif\" $dmy border=0>";
		}
	}
	if ( $found == 0 )	{
		if ( !($icon) )	{	$icon = 0 ;	}
		if ( $icon_gif_w[$icon] != 0 ) { $dmy = "width=\"$icon_gif_w[$icon]\" height=\"$icon_gif_h[$icon]\"" ; } else { $dmy = "" ; }
		print "<img src=\"$icon_gif[$icon]\" $dmy border=0>";
	}
}
###<-------------------------------------------------------------
###<---   ログダウンロードi001112
###<--------------------------------------------------------------
sub download {
    print "Content-type: text/download\n\n";
    print "<html><head><title>$title</title></head>";
	$wk = "bgcolor=\"$bgcolor\"";
	print "<body $wk text=$textcolor link=$linkcolor vlink=$vlinkcolor alink=$alinkcolor>\n";
	&disp ;
	print "<br><br><br>\n";
	&footer ;
    exit;
}
###<--------------------------------------------------------------
###<---   Information
###<--------------------------------------------------------------
sub info	{
	&header ;															#<<<htmlヘッダー出力
	print "<a href=$script>戻る</a>\n";
	print "<center><font size=5><b><<< \昇\進資格 >>></b></font><br><br>\n";
	print "以下の投稿回数に従って、あなたは\昇\進していきます!!<br><br>\n";
	$i =  0;
	print "<table cellpadding=1 cellspacing=0 border=0 bgcolor=#000000><tr><td>\n";
	print "<table cellpadding=5 cellspacing=1 border=0>\n";
	$k = $#rank ;
	for ( @rank )	{
		print "<tr>";
		print "<td align=left width=100 nowrap bgcolor=#ffffff>";
		if ( $acs == 0 ) {
			print "$rank[$i]";
		}	else	{
			print "$rankicon[$i]";
		}
		print "</td>\n";
		print "<td align=right width=150 nowrap bgcolor=#ffffff>";
		$j = $OIWAI[$i+1] - 1 ;
		if ( $i != $k )	{
			print "$OIWAI[$i]&nbsp;～$j&nbsp;回\n";
		}	else	{
			print "$OIWAI[$i]&nbsp;以上\n";
		}
		print "</td>";
		print "<td nowrap bgcolor=#ffffff align=right><img src=\"$rankicon[$i]\"></td>\n" if ( $rankicon[$i] ) ;
		print "<td nowrap bgcolor=#ffffff align=right>&nbsp;</td>\n" if ( !($rankicon[$i]) ) ;
		print "</tr>\n";
		$i++;
	}
	print "</table></td></tr></table></center>";
	&footer ;															#<<<htmlフッター出力
	exit;
}
###<-------------------------------------------------------------
###<---   ランキング取得
###<--------------------------------------------------------------
sub rankget	{
	$set = 0 ;
	$tmax = $#OIWAI ;
	for ( $j = 0 ; $j <= $tmax ; $j++ )	{
		if ( $_[0] >= $OIWAI[$j] )	{
			$ranking = $j ;
		}
	}
	return ($ranking);
}
###<-------------------------------------------------------------
###<---   パスワード暗号化
###<--------------------------------------------------------------
sub pass_enc {
	if ( $ango == 1 ) {
		$pass = crypt($_[0], $_[0]);
	}	else	{
		$pass = $_[0];
	}
}
###<-------------------------------------------------------------
###<---   パスワードチェック
###<--------------------------------------------------------------
sub pass_dec {
	if ( $ango == 1 ) {
		if ($_[0] ne '' && ( crypt($FORM{'pass'}, $_[0]) eq $_[0]) )  {
			return 0 ;
		}
	}	else	{
		if ($FORM{'pass'} eq $_[0]) {
			return 0 ;
		}
	}
	return 1;
}
