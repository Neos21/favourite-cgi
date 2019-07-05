#!/usr/bin/perl
#　☆☆↑↑これをご自分のサーバーの仕様に合わせて変更してね。
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++　　[ あいさつ、しちゃ朗!!  HTML 4.01 Strict Version ] … ver1.1 (2003.9.7)
#+++	
#+++        ･････>>> Edit by Noriya
#+++        Email    >>> pasokon-yugi@syd.odn.ne.jp
#+++　　　　Homepage >>> http://pasokon-yugi.cool.ne.jp/
#+++
#+++		･････>>> Original Script Created by Tacky				     
#+++
#+++		･････>>> Copyright (c) 1999.6 Tacky's Room. All rights reserved....
#+++
#+++        Email    >>> tacky2@ops.dti.ne.jp
#+++        Homepage >>> http://tackysroom.com/
#+++
#+++ 設置方法構成(具体例)
#+++
#+++ public_html（ホームページディレクトリ）
#+++ |
#+++ |-- cgi-bin（任意のディレクトリ）
#+++      |-- credit（アイコンが入っているディレクトリ,755）
#+++  　　|-- yakushoku（アイコンが入っているディレクトリ,755）
#+++   　 |-- jcode.pl      (755)…(日本語ライブラリ)
#+++  　　|-- sicharou.cgi  (755)…(スクリプト本体)
#+++   　 |-- sicharou.txt  (666)…(ログファイル)
#+++   　 |-- sicharou2.txt (666)…(投稿回数管理ファイル)
#+++  　　|-- sicharou3.txt (666)…(常連様用メッセージ格納ファイル)
#+++      |-- orange.gif    (644)…(背景の画像ファイル）
#+++      |-- sicharou.gif  (644)…(タイトル画像ファイル）
#+++ 　　☆　( )内の数字はパーミッッションの値です。　☆
#+++
#+++        画像ファイルはバイナリモード（パーミッションはすべて644）、それ以外はアスキーモードでFTP転送してください。
#+++　　　　画像ファイルは好きなものを使えるよ。いろんな素材配布サイトへ訪れてみよう♪
#+++
#+++ >>> Original Script Update-History...
#+++
#+++    2001.06.12(Ver0.981) >>  ■入力フォームの背景色を指定した場合、名前欄に背景色がつかない不具合修正
#+++    2001.03.12(Ver0.98)  >>  ■お祝いカウント機能に昇進機能を付けました。アイコン付き昇進が可能になりました。
#+++                             ■Locationヘッダーが使えないサーバーの対応。
#+++    2000.12.22(Ver0.974) >>  ■管理人ﾒｯｾｰｼﾞの設定方法の文章ミス。(^^ゞ
#+++    2000.12.20(Ver0.973) >>  ■バージョンアップした場合、連続投稿回数エラーにひっかかる事があるので対処しました
#+++    2000.12.15(Ver0.972) >>  ■連続投稿回数に達してないのにエラーになる場合があった・・・(^-^;
#+++    2000.12.09(Ver0.971) >>  ■連続投稿エラーになった場合でも投稿回数がカウントされる不具合修正
#+++    2000.11.29(Ver0.97)  >>  ■imode対応
#+++                             ■管理人アイコン・常連アイコン設定出来るよ！
#+++                             ■記念カウントによるお祝いメッセージが表示出来るよ！
#+++    2000.07.14(Ver0.96)  >>  ランキング表示部分のFORM開始タグが抜けていた・$footerと表示されている事があった・１行テキストの場合CSSが反映されなかった
#+++    2000.07.12(Ver0.95)  >>  ﾌｧｲﾙﾛｯｸが解除されない場合がある不具合修正
#+++	2000.06.21(Ver0.94)  >>　ﾒﾙｱﾄﾞ&URLを指定しない設定をするとsubmitボタンが２個表示されていました。・textcolorの設定が間違ってました
#+++	2000.06.13  >>　Apache+Netscape文字化け対応・ﾒﾙｱﾄﾞ,URLの指定追加・複数ﾃｷｽﾄ対応・[name]に半角ｽﾍﾟｰｽを入れると半角ｽﾍﾟｰｽ以降認識しないﾊﾞｸﾞ修正
#+++　　　　　　　　　　フォントサイズ指定可能にしました・CSS追加・ロック処理見直し
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

##########################
## 以下、設定項目です。 ##
##########################

require './jcode.pl';										#日本語コード変換
$script 			= "./sicharou.cgi";						#<<<このスクリプトの名前

$URL                = "http://～";                                     #<<<このスクリプトの絶対URL。これをきちんと書いておくと、ページ一番下のリンク「W3C MarkUp Validation Service」から、このCGIが吐き出すHTMLがW3C標準仕様に準拠していることを確認できます（笑）。まあ、趣味の世界ということで…。

$method 			= "POST";								#<<<METHODの指定（POSTで動作しなかったら、GET)
$logfile 			= "./sicharou.txt";						#<<<メッセージのログファイル名
$logfile2 			= "./sicharou2.txt";					#<<<メッセージを登録してくれた方の登録回数累計を保持するファイル
$logfile3 			= './sicharou3.txt';					#<<<メッセージを登録してくれた方々への人別メッセージを登録するファイル
$lockfile			= './sicharou.lock';					#<<<ロックファイルの名前を指定
$title  			= "挨拶しちゃ朗";					#<<<タイトルを指定
$titlelogo 			= "sicharou.gif";		#<<<上段部にタイトルロゴを指定する場合、フルパスで指定。指定しない場合は「""」
$title_w			= "300";					#<<<タイトルロゴの横幅（ピクセル）
$title_h			= "50";					#<<<タイトルロゴの高さ（ピクセル）
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
$textflg_i			= 1 ;									#<<<メッセージ欄の形状。（1:１行テキスト　2:複数行テキスト）
$emailflg_i			= 1 ;									#<<<メールアドレスを入力する？(0:しない 1:する)
$hpflg_i			= 1 ;									#<<<ＵＲＬを入力する？(0:しない 1:する)


#(Webの場合)
$w_name_sz			= 20 ;									#<<<名前欄の文字数
$w_email_sz			= 35 ;									#<<<Email欄の文字数
$w_hp_sz			= 35 ;									#<<<Homepage欄の文字数
$w_message_sz1		= 32 ;									#<<<メッセージ欄の文字数
$w_message_sz2		= 5 ;									#<<<メッセージ欄の行数※１行テキストの場合は対象外
$pagemax 			= 20 ;									#<<<１ページ内に表示する件数
$textflg			= 2 ;									#<<<メッセージ欄の形状。（1:１行テキスト　2:複数行テキスト）
$emailflg			= 1 ;									#<<<メールアドレスを入力する？(0:しない 1:する)
$hpflg				= 1 ;									#<<<ＵＲＬを入力する？(0:しない 1:する)
#####################################
$line1 		= "line1";
$line2 		= "line2";
#============================================================================================================================================
$url 				= "http://～";				#<<<戻り先のURL（通常はあなたのサイトのトップページURL）
$password 			= "password";						#<<<管理者メンテナンス用パスワード（ログ編集用））
$kanriname			= "管理人の名前";								#<<<掲示板管理者の名前（ここに指定された名前は、ランキング対象外となります）
$datamax 			= 200 ;									#<<<最大データ保存件数
$messagemax 		= 50 ;									#<<<来訪者用メッセージの最大件数
$manual 			= 2 ;									#<<<管理人からのメッセージを表示する？(0:no 1:入力ﾌｫｰﾑの下に表示 2:画面下部に表示)

#↓アイコンの指定。$icon_gif[3]...[10]のように適当に増やして下さいね。	※imodeではアイコンは表示出来ません
$icon_flg			= 'yes';								#投稿時にアイコンを使用するか？使用する場合は'yes'と入力する
#↓管理者用アイコンとパスワードを指定。管理人は１つしかアイコン登録出来ません。
#  $oiconnmに指定した名前で投稿した場合、$oicon_gifのアイコンが表示されるようになっています。
#その下は、画像サイズ。_wは幅（ピクセル）。_hは高さ（ピクセル）です。わからない場合は_wの方だけ0にしておいてね。
#管理者アイコンは特に必要無い場合は、$oicon_gif = '';として下さい。
$oicon_gif	  = 'credit/jcb.gif' ;		$oiconnm  = '管理人';
$oicon_gif_w = 32 ; $oicon_gif_h = 32 ; 

#↓常連者用アイコンと投稿時の名前を指定。追加したい時は$jicon_gif[2]...[5]のように増やして下さいね。
#  $jiconnmに指定した名前で投稿した場合、$jicon_gifのアイコンが表示されるようになってます。
#その下は、画像サイズ。_wは幅。_hは高さです。$jicon_gif→アイコンファイル名URL $jiconnm→お名前 $jicon_gif w→アイコンの幅（ピクセル） $jicon_gif_h→アイコンの高さ（ピクセル）

$jicon_gif[0] = 'credit/jcb.gif' ;		$jiconnm[0] = '管理人' ;
$jicon_gif_w[0] = 32 ; $jicon_gif_h[0] = 32 ;

#続き　[]内の数字を変えればいくつでも登録できます。下の1番を使う時は、先頭の#を外してご利用下さい。 
#$jicon_gif[1] = '' ;	$jiconnm[1] = '';
#$jicon_gif_w[1] = 32 ; $jicon_gif_h[1] = 32 ; 

$icon_imode			= 7	;
#imodeからのアクセスの場合、固定で１個だけ下記のアイコンの番号を選択してください。

#訪問者用アイコンとアイコンの名前の指定。$icon_gif[3]...[10]のように適当に増やして下さいね。
#その下は、画像サイズ。_wは幅。_hは高さです。

$icon_gif[0] = 'credit/amex.gif' ;		$iconnm[0] = 'アメックス' ;
$icon_gif_w[0] = 32 ; $icon_gif_h[0] = 32 ; 
$icon_gif[1] = 'credit/aplus.gif' ;		$iconnm[1] = 'アプラス' ;
$icon_gif_w[1] = 32 ; $icon_gif_h[1] = 32 ;
$icon_gif[2] = 'credit/cf.gif' ;		$iconnm[2] = 'CFカード' ;
$icon_gif_w[2] = 32 ; $icon_gif_h[2] = 32 ;
$icon_gif[3] = 'credit/aeon.gif' ;	$iconnm[3] = 'イーオン' ;
$icon_gif_w[3] = 32 ; $icon_gif_h[3] = 32 ;
$icon_gif[4] = 'credit/acom.gif' ;	$iconnm[4] = 'アコム' ;
$icon_gif_w[4] = 32 ; $icon_gif_h[4] = 32 ;
$icon_gif[5] = 'credit/dc.gif' ;		$iconnm[5] = 'DCカード' ;
$icon_gif_w[5] = 32 ; $icon_gif_h[5] = 32 ;
$icon_gif[6] = 'credit/aiful.gif' ;	$iconnm[6] = 'アイフル' ;
$icon_gif_w[6] = 32 ; $icon_gif_h[6] = 32 ;
$icon_gif[7] = 'credit/dic.gif' ;	$iconnm[7] = 'ディック' ;
$icon_gif_w[7] = 32 ; $icon_gif_h[7] = 32 ;
$icon_gif[8] = 'credit/jaccs.gif' ;	$iconnm[8] = 'ジャックス' ;
$icon_gif_w[8] = 32 ; $icon_gif_h[8] = 32 ;
$icon_gif[9] = 'credit/jcb.gif' ;	$iconnm[9] = 'JCB' ;
$icon_gif_w[9] = 32 ; $icon_gif_h[9] = 32 ;
$icon_gif[10] = 'credit/lake.gif' ;	$iconnm[10] = 'レイク' ;
$icon_gif_w[10] = 32 ; $icon_gif_h[10] = 32 ;
$icon_gif[11] = 'credit/master.gif' ;	$iconnm[11] = 'マスター' ;
$icon_gif_w[11] = 32 ; $icon_gif_h[11] = 32 ;
$icon_gif[12] = 'credit/million.gif' ;	$iconnm[12] = 'ミリオン' ;
$icon_gif_w[12] = 32 ; $icon_gif_h[12] = 32 ;
$icon_gif[13] = 'credit/nicos.gif' ;		$iconnm[13] = 'ニコス' ;
$icon_gif_w[13] = 32 ; $icon_gif_h[13] = 32 ;
$icon_gif[14] = 'credit/visa.gif' ;	$iconnm[14] = 'VISA' ;
$icon_gif_w[14] = 32 ; $icon_gif_h[14] = 32 ;
$icon_gif[15] = 'credit/orico.gif' ;	$iconnm[15] = 'オリコ' ;
$icon_gif_w[15] = 32 ; $icon_gif_h[15] = 32 ;
$icon_gif[16] = 'credit/orix.gif' ;	$iconnm[16] = 'オリックス' ;
$icon_gif_w[16] = 32 ; $icon_gif_h[16] = 32 ;
$icon_gif[17] = 'credit/promise.gif' ;	$iconnm[17] = 'プロミス' ;
$icon_gif_w[17] = 32 ; $icon_gif_h[17] = 32 ;
$icon_gif[18] = 'credit/saison.gif' ;		$iconnm[18] = 'セゾン' ;
$icon_gif_w[18] = 32 ; $icon_gif_h[18] = 32 ;
$icon_gif[19] = 'credit/uc.gif' ;		$iconnm[19] = 'UCカード' ;
$icon_gif_w[19] = 32 ; $icon_gif_h[19] = 32 ;

#アイコン一覧を表示する際、１行にアイコンを何個表示します？
$icon_line					= 5 ;	#←の場合、5個表示したら改行するって事です。

#<<<Webからのアクセス時、画面下部に表示する「管理人からのメッセージ」。"EOM"～EOMの行までに必ず入れてください。メッセージ不要の場合は、$manualmsgの行からEOMの行まで全て削除してね
$manualmsg = <<"EOM";
<p class="setsumei">おはこんばー！僕「しちゃ朗」は何かと\申\しますと、コミュニケーションをとる為にとっても大切な事、そう!!『挨拶』です!!....挨拶しましょ～！ただそれだけ。（笑） 僕の使い方は「名前を書いて、ポン♪　押すだけぇ～♪」で～す。</p>

<p class="setsumei">※補足：『おはこんば～♪』は、みなさんがいつ挨拶してくれるかわからないから、「おはよう」、「こんにちは」、「こんばんわ」をミックスしてみました～♪（笑） iModeでも見られます。（たぶん…）</p>
EOM

#<<<imodeからのアクセス時、画面下部に表示する管理者からのメッセージ。"EOM"～EOMの行までに必ず入れてください。メッセージ不要の場合は、$manualmsg2の行からEOMの行まで全て削除してね
$manualmsg2 = <<"EOM";
<p>みんな気軽に書き込みしてね～♪</p>
EOM

@errtag = ('table','meta','form','!--','embed','html','body','tr','td','th','a');		#デンジャラ～なタグ

#=============================================================================================================================================================================================

$rankcnt					= 30 ;	#ランキング上位何人をランキング一覧画面に表示しますか？

#お祝いカウント設定。指定した投稿回数に達すると、お祝いメッセージを表示します。不要の場合は、@OIWAIの行を削除してね。

@OIWAI = (0,10,30,50,80,120,170,230,300,400,600,1000,1500,2500,4000);

#お祝いメッセージ表示の際の文章。NAMEとCNTの部分にはその人の名前と達成回数が置換されますので、
#必ずNAME・CNTという文字は入れておいてください。

$oiwaimsg = "NAMEさん!! 投稿回数がCNT回に達成し昇進しました!!!!!";

#掲示板荒らし対策。排除したいプロバのアドレスを設定して下さい。
#　"xxx?.com"とした場合、"xxx1.com","xxx2.com"等、「？」の部分が文字列１つと判断します
#  "xxx*.com"とした場合、"xxx1.com","xxx12345.com等、「＊」の部分が０個以上の文字列と判断します。
#例：@DANGER_LIST=("xxx.com","yyy.com","zzz*.or.jp");

@DANGER_LIST=("","","");

#掲示板荒らし対策その２。メッセージ最大文字数を指定。特に設定しない場合は、''として下さい。

$maxword = '1000' ;

$renchan1		= 1 ;		#指定分以内の連続投稿はｴﾗｰとする。設定しない場合は0としてね。
$renchan2		= 4 ;		#指定回数以上の連続投稿はｴﾗｰとする。設定しない場合は0としてね。

$method 			= "POST";								#<<<METHODの指定（POSTで動作しなかったら、GET)

#↓上記にある「@OIWAI」に指定した回数で昇進していきます。@OIWAIと同じ個数分設定して下さい。
@rank	= ('幼稚園生','小学校低学年','小学校中学年','小学校高学年','中学生','高校生','大学生','平社員','係長','課長','部長','常務','専務','社長','会長');

#↓昇進に画像を使う場合、昇進回数と同じ個数分設定してください。※$rankicon[n]は必ず「0」から始まります。画像を使わない部分は''としてね。
#　画像の幅・高さがわからない人は、$rankicon_w[n] = 0 ; $rankicon_h[n] = 0 ;のように「0」として下さい。

$rankicon[0] = '' ;	$rankicon_w[0] = 0 ; $rankicon_h[0] = 0 ;
$rankicon[1] = '' ;	$rankicon_w[1] = 0 ; $rankicon_h[1] = 0 ;
$rankicon[2] = '' ;	$rankicon_w[2] = 0 ; $rankicon_h[2] = 0 ;
$rankicon[3] = '' ;	$rankicon_w[3] = 0 ; $rankicon_h[3] = 0 ;
$rankicon[4] = 'yakushoku/madogiwa.gif' ;	$rankicon_w[4] = 32 ; $rankicon_h[4] = 32 ;
$rankicon[5] = 'yakushoku/hantyou.gif' ;	$rankicon_w[5] = 32 ; $rankicon_h[5] = 32 ;
$rankicon[6] = 'yakushoku/syunin.gif' ;	$rankicon_w[6] = 32 ; $rankicon_h[6] = 32 ;
$rankicon[7] = 'yakushoku/taityou.gif' ;	$rankicon_w[7] = 32 ; $rankicon_h[7] = 32 ;
$rankicon[8] = 'yakushoku/kakarityou.gif' ;	$rankicon_w[8] 	= 32 ; $rankicon_h[8] = 32 ;
$rankicon[9] = 'yakushoku/katyou.gif' ;		$rankicon_w[9] 	= 32 ; $rankicon_h[9] = 32 ;
$rankicon[10] = 'yakushoku/butyou.gif' ;	$rankicon_w[10] = 32 ; $rankicon_h[10] = 32 ;
$rankicon[11] = 'yakushoku/zyoumu.gif' ;	$rankicon_w[11] = 32 ; $rankicon_h[11] = 32 ;
$rankicon[12] = 'yakushoku/senmu.gif' ;		$rankicon_w[12] = 32 ; $rankicon_h[12] = 32 ;
$rankicon[13] = 'yakushoku/syatyou.gif' ;	$rankicon_w[13] = 32 ; $rankicon_h[13] = 32 ;
$rankicon[14] = 'yakushoku/kaityou.gif' ;	$rankicon_w[14] = 32 ; $rankicon_h[14] = 32 ;

$damedame		= 0 ;	#Locationヘッダが使えないサーバーは1。通常は0でいいはず。※トクトク、3nopage,WinNTサーバー等が1かな。

#####################################################
##                                                 ##
##　ここから下はいじらない方が身のためです。(^_^;  ##
##                                                 ##
#####################################################

utime time(), time(), __FILE__; 								# スクリプト生成日時の更新

#■■■WebからのアクセスからかiMODEからのアクセスかを判断
$agent = $ENV{'HTTP_USER_AGENT'};
if ( $agent =~ /docomo/i )	{	
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
if ($ENV{'HTTP_USER_AGENT'} !~ /MSIE/i || $acs == 1 ) { $css_style = "" ; }		#Netscape-CSS対応

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

if ($ENV{'HTTP_USER_AGENT'} !~ /MSIE/i) {	$css_style = "" ;	}		

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
		}
		&dataread ;
	}
	&header ;						   			#<<<htmlヘッダーの出力
	&inputform ; 				       			#<<<入力フォームの表示
	&disp ;							   			#<<<登録済メッセージの表示
	if ( $manual == 2 )	{	&setumei;	}	#<<<「使い方」の表示
	print "\n<form action=\"$script\" method=\"$method\">\n";
	print "<dl class=\"password\">\n";
	if ( $acs == 0 ) { print "<dt>No</dt>\n";	}
	print "<dd><input type=\"text\" name=\"no\" size=\"4\"></dd>\n";
	if ( $acs == 1 ) { print "<dt>No</dt>\n";	}
	if ( $acs == 0 ) { print "<dt>Pass</dt>\n";	}
	print "<dd><input type=\"password\" name=\"pass\" size=\"8\"></dd>\n";
	if ( $acs == 1 ) { print "<dt>Pass</dt>\n";	}
	print "<dt><select name=\"proc\">\n";
	print "<option value=\"edit\">編集\n";
	print "<option value=\"delete\">削除\n";
	print "<option value=\"message\">訪問者メッセージ\n";
	print "</select>\n</dt>\n";
	if ( $acs == 1 ) { print "";	}
	print "<dd><input type=\"hidden\" name=\"action\" value=\"maintenance\">\n";
	print "<input type=\"submit\" value=\"ADMIN\"></dd>\n</dl>\n";
	#<<<　↓消さないでネ♪
	print "<ul class=\"ScriptAuthor\">\n<li><a href=\"http://tackysroom.com/\">sicharou(Ver0.981)-Tacky</a></li>\n<li>Edit by <a href=\"http://pasokon-yugi.cool.ne.jp/\">Noriya@ぱそこんゆうぎ</a></li>\n";
    print "<li><a href=\"http://validator.w3.org/check?uri=$URL\">W3C MarkUp Validation Service</a></li>\n</ul>\n";
	print "</form>\n\n";
	print "" if ( $acs == 0 );	
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
		read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
	} else { $buffer = $ENV{'QUERY_STRING'}; }
	@pairs = split(/&/,$buffer);
	@msg = ();
	foreach $pair (@pairs) {
		($name, $value) = split(/=/, $pair);
		$value =~ tr/+/ /;
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		foreach ( @errtag )	{
			if ($value =~ /<$_(.|\n)*>/i) {	 &error("使用出来ないタグが入力されています");	}
		}
		$value =~ s/\,/，/g;
		&jcode'convert(*value,'sjis');
		$FORM{$name} = $value;
	}
	$FORM{'com'} =~ s/\r\n/<br>/g;	$FORM{'com'} =~ s/\r|\n/<br>/g;	
	$FORM{'hp'}   =~ s/^http\:\/\///;
	if ( $acs == 1 )	{	$FORM{'icon'} = $icon_imode ;	}
}
###<--------------------------------------------------------------
###<---   HTMLヘッダー書き出し
###<--------------------------------------------------------------
sub	header	{
	print "Content-type: text/html; charset=Shift_JIS\n\n";
	print "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\">\n";
	print "<html lang=\"ja\">\n<head>\n";
	print "<meta http-equiv=\"Content-type\" content=\"text/html; charset=Shift_JIS\">\n";
	print "<meta http-equiv=\"content-style-type\" content=\"text/css\">\n<meta http-equiv=\"content-script-type\" content=\"text/javascript\">\n";
	print "<title>$title</title>\n";
	print "<link rel=\"stylesheet\" type=\"text/css\" href=\"sicharou.css\" media=\"all\">\n";
	print "</head>\n\n";
	print "<body>\n\n";
}
###<--------------------------------------------------------------
###<---   HTMLフッダー書き出し
###<--------------------------------------------------------------
sub footer { 
	print "</body>\n</html>\n";
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
###<---   入力フォーム
###<--------------------------------------------------------------
sub	inputform	{
	if ( $acs == 0 )	{
		print "<form action=\"$script\">\n";
		print "<ul class=\"navi\">\n";
		print "<li><input type=\"button\" VALUE=\"HOME\" ";
		print "onClick=\"parent.location.href=\'$url\'\"></li>\n";
		if ( $logfile2 && $FORM{'action'} ne 'download')	{	#i001112
#			print "<form>\n";	#i000714
			print "<li><INPUT TYPE=\"button\" VALUE=\"ランキング\" ";
			print "onClick=\"parent.location.href=\'$script?action=ranking\'\"></li>\n";
		}
		if ( $logfile2 && $FORM{'action'} ne 'download')	{
#			print "<form>\n";
			print "<li><INPUT TYPE=button VALUE=\"昇進資格説明\" ";
			print "onClick=\"parent.location.href=\'$script?action=info\'\"></li>\n";
		}
		print "</ul>\n</form>\n\n";
	}	else	{
		if ( $url )	{	print "<ul>\n<li><a href=\"$url\">HOME</a></li>\n";	}
		if ( $logfile2 && $FORM{'action'} ne 'download')	{	#i001112
			print "<li><a href=\"$script?action=ranking\">ランキング</a></li>\n";
		}
		print "</ul>\n";
	}
	if ( $titlelogo )	{
		print "<h1><img src=\"$titlelogo\" alt=\"$title\" width=\"$title_w\" height=\"$title_h\"></h1>\n\n";
	}	else	{
		print "<h1>$title</h1>\n\n";
	}
	print "<form name=\"inputform\" action=\"$script\" method=\"$method\">\n";
	if ( $FORM{'action'} ne 'maintenance' )	{
		print "<p><input type=\"hidden\" name=\"action\" value=\"regist\"></p>\n\n";
	}	else	{
		print "<p><input type=\"hidden\" name=\"action\" value=\"update\"></p>\n";
		print "<p><input type=\"hidden\" name=\"no\" value=\"$FORM{'no'}\"></p>\n";
		print "<p><input type=\"hidden\" name=\"proc\" value=\"edit\"></p>\n";
	}
#=================================================================
#通常ウェブサイトならば
	if ( $acs == 0 )	{
#$textflgここから
	if ( $textflg != 1 )	{
		#■お名前
		print "<div class=\"input\">\n<dl>\n<dt>Name</dt>\n";
		print "<dd><input type=\"text\" name=\"name\" size=\"$name_sz\" value=\"$c_name\"></dd>\n";
#■アイコン
		if ( $icon_flg eq 'yes' )	{
			print "<dt>Icon</dt>\n<dd><select name=\"icon\">\n";
			for ( $i = 0 ; $i <= $#iconnm ; $i++ ) {
				if ( $i == $c_icon )	{	$dmy = "selected";	}	else	{	$dmy = "" ;	} 
				print "<option value=\"$i\">$iconnm[$i]</option>\n";
			}
#■アイコンここまで
			print "</select></dd>\n";
		}
#$textflgここまで
		if ( $emailflg == 1 ) { 
			#■メールアドレス
			print "<dt>Email</dt>\n<dd><input type=\"text\" name=\"email\" size=\"$email_sz\" value=\"$c_email\"></dd>\n";
		}
		if ( $hpflg == 1 ) { 
			#■Homepage
			print "<dt>URL</dt>\n<dd><input type=\"text\" name=\"hp\" size=\"$hp_sz\" value=\"http://$c_hp\"></dd>\n";
		}
		print "<dt>Comment</dt>\n";
		print "<dd><textarea name=\"com\" cols=\"$message_sz1\" rows=\"$message_sz2\">$c_cm</textarea></dd>\n</dl>\n";
		print "<ul id=\"submit\">\n<li><input type=\"submit\" value=\"$submit\"></li>\n";
		if ( $icon_flg eq 'yes' )	{	print "<li><a href=\"$script?action=icondisp\">アイコン一覧</a></li>\n</ul>\n</div>\n";	}

	}	else	{
		if ( $emailflg == 1 || $hpflg == 1 )	{
			if ( $icon_flg eq 'yes' )	{
				print "";
			}
		}
		print "<div class=\"input\">\n<dl>\n<dt>Name</dt>\n";
		print "<dd><input type=\"text\" name=\"name\" size=\"15\" value=\"$c_name\"></dd>\n";
		if ( $icon_flg eq 'yes' )	{
			print "<dt>Icon</dt>\n<dd><select name=\"icon\">\n";
			for ( $i = 0 ; $i <= $#iconnm ; $i++ ) {
				if ( $i == $c_icon )	{	$dmy = "selected";	}	else	{	$dmy = "" ;	} 
				print "<option value=\"$i\">$iconnm[$i]</option>\n";
			}
			print "</select>\n</dd>\n";
		}
		if ( $emailflg == 0 && $hpflg == 0 )	{
		}	else	{
			if ( $emailflg == 1 ) { 
				print "<dt>Email</dt>\n<dd><input type=\"text\" name=\"email\" size=\"$email_sz\" value=\"$c_email\"></dd>\n";
			}
			if ( $hpflg == 1 ) { 
				print "<dt>URL</dt>\n<dd><input type=\"text\" name=\"hp\" size=\"$hp_sz\" value=\"http://$c_hp\"></dd>\n";
			}
		}
		print "<dt>Comment</dt>\n";
		print "<dd><input type=\"text\" name=\"com\" size=\"$message_sz1\" value=\"$c_cm\"></dd>\n</dl>\n";
		print "<ul id=\"submit\">\n<li><input type=\"submit\" value=\"$submit\"></li>\n\n";
			if ( $icon_flg eq 'yes' )	{
				print "<li><a href=\"$script?action=icondisp\">アイコン一覧</a>";
			}

		print "</ul>\n</div>\n\n";

	}
	}	else	{		#imode時
		#■お名前
		print "<dl>\n<dt>Name</dt>";
		print "<dd><input type=\"text\" name=\"name\" size=\"$name_sz\" value=\"$c_name\"></dd>\n";
		if ( $emailflg == 1 ) { 
			#■メールアドレス
			print "<dt>Email</dt>\n<dd><input type=\"text\" name=\"email\" size=\"$email_sz\" value=\"$c_email\"></dd>\n";
		}
		if ( $hpflg == 1 ) { 
			#■Homepage
			print "<dt>URL</dt>\n<dd><input type=\"text\" name=\"hp\" size=\"$hp_sz\" value=\"http://$c_hp\"></dd>\n";
		}
		print "<dt>Message</dt>\n";
		if ( $textflg != 1 )	{
			print "<dd><textarea name=\"com\" cols=\"$message_sz1\" rows=\"$message_sz2\">$c_cm</textarea></dd>";
		}	else	{
			print "<dd><input type=\"text\" name=\"com\" size=\"$message_sz1\" value=\"$c_cm\"></dd>\n";
		}
		print "<dd><input type=\"submit\" value=\"$submit\"></dd>\n</dl>\n";
	}
	print "</form>\n\n";

	if ( $manual == 1 )	{	&setumei;	}	#<<<「使い方」の表示

	print "" if ( $acs == 0 ) ;
	if ( $acs == 0 )	{
		print "<SCRIPT type=\"text/JavaScript\">\n";
		print "<!--\n";
		if ( $c_name eq "" ) 	{
			print "document.inputform.name.focus();\n";
		}	else	{	
			print "document.inputform.com.focus();\n";
		}
		print "// -->\n";
		print "</SCRIPT>\n\n";
	}
}
###<--------------------------------------------------------------
###<---   みなさんからの挨拶を表示
###<--------------------------------------------------------------
sub	disp	{

	if ( $acs == 0 )	{
		print "<h1>$title</h1>\n" if ( $FORM{'action'} eq 'download' ) ;;
		if ( !(open(IN3,"$logfile3")))	{	&error("ログファイル３($logfile3)のオープンに失敗しました");	}
		@message = <IN3>;
		close(IN3);
		foreach ( @message ) {
			($n,$m) = split(/:/,$_);
			if ( $c_name eq $n )	{
				print "<div class=\"adminmessage\">\n<h2>管理人からのメッセージ</h2>\n<p>\n$m</p>\n</div>\n\n";
			}
		}
		print "<table summary=\"皆さんのご挨拶\">\n";
		print "<caption>皆さんのご挨拶一覧</caption>\n";
		print "<tr class=\"header\">\n<th class=\"number\">No</th>\n";
		print "<th class=\"date\">Date</th>\n";
		print "<th class=\"name\">Name</th>\n";
		if ( $icon_flg eq 'yes' && $FORM{'action'} ne 'download' )	{
			print "<th class=\"icon\">Icon</th>\n";
		}
		if ( $hpflg == 1 )	{	print "<th class=\"url\">Site</th>\n";	}
		print "<th class=\"message\">Message</th>\n";
		if ( $logfile2 )	{
			print "<th class=\"kaisu\">回数</th>\n";
			print "<th class=\"shoshin\">役職</th>\n";
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
			if ( $bg eq $line1 ) {			$bg = $line2;
			}	else	{			$bg = $line1;		}
			print "<tr class=\"$bg\">\n<td class=\"number\">$no</td>\n";
			if ( $cm ne 'OIWAI' )	{
				print "<td class=\"date\">$edt-$svtime</td>\n";
				print "<td class=\"name\">";
				if ( $email ) {
					print "<a href=\"mailto:$email\">$nm</a>";
				}	else	{
					print "$nm";
				}
				print "</td>\n";
				if ( $icon_flg eq 'yes' )	{
					print "<td class=\"icon\">";
					&icon_set($nm) ;
					print "</td>\n";
				}
				if ( $hpflg == 1 )	{
					print "<td class=\"url\">";
					if ( $hp )	{	print "<a href=\"http://$hp\"><img src=\"home.gif\" alt=\"website\" width=\"25\" height=\"22\"></a></td>\n";	}
					else	{	print "&nbsp;</td>\n";	}
				}
				if ( $cm eq '' ) {	$cm = '　';	}
				print "<td class=\"message\">$cm</td>\n";
				if ( $logfile2 )	{	#i001112
					print "<td class=\"kaisu\">$raihoucnt</td>\n";
					$ranking = &rankget($raihoucnt) ;
					print "<td class=\"shoshin\">";
					print "<img src=\"$rankicon[$ranking]\" alt=\"役職\" width=\"$rankicon_w[$ranking]\" height=\"$rankicon_h[$ranking]\">\n" if ( $rankicon[$ranking] ) ;
					print "$rank[$ranking]\n" if ( !($rankicon[$ranking]) ) ;
					print "</td>\n";
				}
				print "</tr>\n";
			}	else	{
				$cs = 7 ;
				if ( $icon_flg ne 'yes' )	{	$cs--;	}
				if ( $hpflg != 1 )	{	$cs--;	}
				if ( $logfile2 eq '' )	{	$cs--;	}
				print "<td colspan=\"$cs\" class=\"oiwai\">\n";
				$wk = $oiwaimsg ;
				$wk =~ s/NAME/$nm/i;	$wk =~ s/CNT/$raihoucnt/i;
				print "$wk";
				print "</td>\n</tr>\n";
			}
		}	else	{
			print "<hr>";
			print "[$no]..$edt-$svtime<br>\n";
			if ( $email ) {
				print "<a href=mailto:$email>$nm</a>\n";
			}	else	{
				print "$nm";
			}
			if ( $logfile2 )	{	#i001112
				$ranking = &rankget($raihoucnt) ;
				print "($raihoucnt回…$rank[$ranking])\n";
			}
			if ( $hpflg == 1 )	{
				if ( $hp )	{	print "<a href=\"http://$hp\">-[URL]</a>\n";	}
			}
			print "";
			if ( $cm eq '' ) {	$cm = '　';	}
			print "$cm\n";
		}
		$z++;
	}
	print "</table>\n\n" if ( $acs == 0 );
	if ( $FORM{'action'} ne 'download' )	{	#i001112
		print "<form action=\"$script\" method=\"$method\">\n";
		print "<p><input type=\"hidden\" name=\"disppage\" value=\"$FORM{'disppage'}\"></p>\n";
		print "<ul class=\"navi2\">\n";
		if ( $FORM{'disppage'} != 0 && $FORM{'disppage'} !=1)	{
			print "<li><input type=\"submit\" name=\"page\" value=\"BACK\"></li>\n";
		}	
		if ( $FORM{'disppage'} + 1 <= $p )	{
			print "<li><input type=\"submit\" name=\"page\" value=\"NEXT\"></li>\n";
		}
		print "</ul>\n</form>\n\n";
	}
	if ( $acs == 0 )	{
		if ( $logfile2 )	{	#i001112
			print "<p class=\"totalcount\">TotalCountは、あなたの過去からの挨拶回数です♪</p>\n\n";
		}
	}	else	{
		print "<p>( )の数字は投稿回数です</p>\n";
	}
	if ( $acs == 0 )	{	#i001112
		print "" ;
		print "<form action=\"$script\" method=\"$method\" class=\"logdownload\">\n";
		print "<ul class=\"download\">\n<li><input type=\"hidden\" name=\"action\" value=\"download\">\n";
		print "<input type=\"submit\" value=\"ログをダウンロード\"></li>\n</ul>\n";
		print "<p class=\"caution\">ダウンロードしたファイルの拡張子を .cgi → .html に変更して下さいね♪</p>\n";
		print "</form>\n";
	}
}
###<--------------------------------------------------------------
###<---   挨拶ログ出力
###<--------------------------------------------------------------
sub	regist	{
	if ( $FORM{'name'} eq "")	{	&error("名前は省略出来ません。") ;	}
	if ( $maxword ne '' && (length($FORM{'com'}) > $maxword))	{	&error("メッセージは$maxword文字までしか登録出来ません。");	}
	if ( $textflg2 == 1 && $FORM{'com'} eq '' )	{	&error("メッセージ欄は省略出来ません。") ;	}

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
			if($host =~ /$buf/gi){	&error("\申\し\訳ありません。<br>あなたのプロバイダーからは投稿できませんでした。");	}
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

	unshift(@LOG,"$no,$today,$FORM{'name'},$FORM{'com'},$dcnt,$FORM{'icon'},$FORM{'email'},$FORM{'hp'},$host,\n");

foreach $buf ( @OIWAI )	{
		if ( $dcnt == $buf )	{
			$dcnt2 = @LOG;
			if ($dcnt2 >= $datamax) {	pop(@LOG);	}
			$no++ ;
			unshift(@LOG,"$no,$today,$FORM{'name'},OIWAI,$dcnt,$FORM{'email'},,$host,\n");
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
		($FORM{'name'}, $value) = split(/=/, $pair);
		$FORM{'name'} =~ s/ //g;
		$DUMMY{$FORM{'name'}} = $value;
	}
	@pairs = split(/,/,$DUMMY{'sicharou'});
	foreach $pair (@pairs) {
		($FORM{'name'}, $value) = split(/\!/, $pair);
		$COOKIE{$FORM{'name'}} = $value;
	}
	$c_name  = $COOKIE{'nm'};
	$c_icon  = $COOKIE{'icon'};
	$c_email  = $COOKIE{'em'};
	$c_hp  = $COOKIE{'hp'};
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
	$cook="nm\!$FORM{'name'},icon\!$FORM{'icon'},em\!$FORM{'email'},hp\!$FORM{'hp'}";
	print "Set-Cookie: sicharou=$cook; expires=$date_gmt\n";
}
###<--------------------------------------------------------------
###<---   メンテナンスモード
###<--------------------------------------------------------------
sub Maintenance {
	if ( $FORM{'proc'} ne 'message' && $FORM{'no'} eq "")	{	&error("メンテナンス対象の記事Noを指定して下さい。");	}
	if ( $FORM{'pass'} eq "")	{	&error("パスワードを入力して下さい。");	}
	if ( $FORM{'pass'} ne $password)	{	&error("パスワードが違います。") ;	}

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
		($no,$dt,$nm,$cm,$cnt,$icon,$email,$hp,$hst,$dmy) = split(/,/,$_);
		if ( $FORM{'no'} eq $no )	{		
			$found = 1 ;
			if ( $FORM{'proc'} eq "delete" )	{
				&update ;
				exit;
			}
			&header ;
			$c_name = $nm ;	$c_icon = $icon ;	$c_email = $email ;	$c_hp = $hp ;
			$c_cm = $cm ; $c_cm =~ s/\<br\>/\n/g;
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
	print "<ul class=\"back\">\n<li><a href=\"$script\">BACK</a></li>\n</ul>\n";
if ( $acs == 0 )	{
print <<"EOM";
<h1>■来訪者毎に特定のメッセージを表\示する設定■</h1>

<p>来訪者がクッキーを許可している場合、ここで登録した名前の人がアクセスした際に設定したメッセージが表\示されます。</p>

<p>設定方法は、「訪問者の名前」+「:（半角コロン）」＋「表\示メッセージ」＋「改行」でお一人様のメッセージとなります。</p>

<p>文章の途中で改行した場合はメッセージに&lt;br&gt;を入れて設定して下さい。</p>

<dl>
<dt>例：</dt>
<dd>Ａさん:いつも来てくれてありがとう</dd>
<dd>Ｂさん:しばらく来てないねぇ・・・</dd>
<dd>Ｃさん:Ｃさんへ！&lt;em&gt;誕生日おめでとー!!!&lt;/em&gt;</dd>
<dd>※タグを挿入可能\です。</dd>
</dl>
EOM
}	else	{
print <<"EOM";
<h1>■来訪者毎のメッセージ設定■</h1>

<p>「訪問者の名前」+「:（半角コロン）」＋「表\示メッセージ」＋「改行」でお一人様のメッセージとなります。</p>

<p>文章の途中で改行した場合はメッセージに&lt;br&gt;を入れて設定して下さい。</p>
EOM
}
	foreach ( @data )	{ 
		($nm,$cm) = split(/:/,$_);
		$cm =~ s/\n//;
		if ($nm eq '' || $cm eq '') { next; } #i001215
		$BUF .= "$nm:$cm\r";
	}
	print "<form action=\"$script\" method=\"$method\">\n";
	print "<dl>\n<dt><input type=\"hidden\" name=\"action\" value=\"update2\">\n";
	if ( $acs == 0 )	{
		print "<textarea name=\"msg\" cols=\"70\" rows=\"10\">$BUF</textarea></dt>\n";
		print "<dd><input type=\"submit\" value=\"訪問者メッセージを更新する\"></dd>\n</dl>\n";
		print "</form>\n";
	}	else	{
		print "<textarea name=\"msg\" cols=\"$message_sz1\" rows=\"$message_sz2\">$BUF</textarea>\n";
		print "<input type=\"submit\" value=\"更新\">\n";
		print "</form>\n";
	}
	&footer ;
	exit ;
}
###<--------------------------------------------------------------
###<---   ログファイル更新
###<--------------------------------------------------------------
sub update {

	&filelock ;		#ファイルロック
	&dataread ;
    foreach (@LOG) {
		($no,$dt,$nm,$cm,$cnt,$icon,$email,$hp,$hst,$dmy) = split(/,/,$_);
        if ($FORM{'no'} eq $no ) {									#<<<編集対象データの場合
			if ( $FORM{'proc'} ne 'delete' )	{
				push(@new,"$no,$dt,$FORM{'name'},$FORM{'com'},$cnt,$FORM{'icon'},$FORM{'email'},$FORM{'hp'},$hst,$dmy");			#編集後の内容で置換
			}
		}	else	{										#<<<編集対象データ以外の場合
			$found = 0 ;
			if ( $FORM{'proc'} eq 'delete' ) {
				@DELWORD = split(/ /,$FORM{'no'});
				foreach $word ( @DELWORD )	{	
					if ( $word && ( $no == $word ) ) { $found = 1 ; last ; }
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
	print "<ul class=\"back\">\n<li><a href=\"$script\">戻る</a></li>\n</ul>\n";

	@Lank = ();
    foreach $buf (@data) {
		($a,$b) = split(/,/,$buf);
		push(@Lank,"$b,$a");		
	}
	@Lank = sort { $a <=> $b } @Lank ;
	@Lank = reverse @Lank ;
	print "" if ( $acs == 0 ) ;
	print "<h1>&lt;&lt;&lt;&lt;&lt; ランキング &gt;&gt;&gt;&gt;&gt;</h1>\n";
	$c = $totalcount ;
	print "<p class=\"tokoshasu\">総投稿者数==&gt;$c人</p>\n"; 
	if ( $acs == 0 )	{
		print "<table summary=\"投稿者上位\" class=\"ranking\">\n<tr class=\"header\">\n";
		print "<th>ランキング</th>\n";
		print "<th>お名前</th>\n";
		print "<th>投稿回数</th>\n";
		print "<th>昇進状態</th>\n</tr>\n";
	}
	$cnt=1;
	foreach $buf ( @Lank )	{
		($raihoucnt,$nm) = split(/,/,$buf);
		if ( $nm ne $kanriname)	{
			if ( $bg eq $line1 ) {
				$bg = $line2;
			}	else	{
				$bg = $line1;
			}
			$raihoucnt = sprintf("%d",$raihoucnt);
			for ( $j = 0 ; $j <= $#OIWAI ; $j++ )	{
				if ( $raihoucnt >= $OIWAI[$j] )	{
					$ranking = $j ;
				}
			}
			if ( $acs == 0 )	{
				print "<tr class=\"$bg\">\n<td>$cnt位</td>\n";
				print "<td>$nm</td>\n";
				print "<td>$raihoucnt回</td>\n";
				print "<td><img src=\"$rankicon[$ranking]\" alt=\"Ranking\" width=\"$rankicon_w[$ranking]\" height=\"$rankicon_h[$ranking]\"></td>\n" if ( $rankicon[$ranking] ) ;
				print "<td>$rank[$ranking]</td>\n" if ( !($rankicon[$ranking]) ) ;
				print "</tr>\n";
			}	else	{
				print "$cnt位：$nm($raihoucnt回…$rank[$ranking])<br>";
			}
			$cnt++ ;
		}
		if ( $cnt > $rankcnt ) {	last ;	}
	}
	if ( $acs == 0 ) {
		print "</table>\n";
		print "" ;
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
	print "<ul class=\"back\">\n<li><a href=\"$script\">戻る</a></li>\n</ul>\n";
	print "<h1>■■■ アイコン一覧 ■■■</h1>\n";
	print "<table cellpadding=\"5\" cellspacing=\"0\" summary=\"アイコン一覧\" class=\"iconlist\">\n";
	$i = 0 ; $j = 0 ;
	while ( 1 )	{
		print "<tr>\n";
		for ( $ln = 1 ; $j <= $#icon_gif && $ln <= $icon_line ; ) {
			print "<td><img src=\"$icon_gif[$j]\" alt=\"icon\" width=\"$icon_gif_w[$j]\" height=\"$icon_gif_h[$j]\"></td>\n";
			print "<td>$iconnm[$j]</td>\n";
			$j++ ; $ln++ ;
		}
		if ( $j > $#icon_gif ) { 
			if ( $ln < $icon_line ) {
				for ( ; $ln <= $icon_line ; ) {
					print "<td>&nbsp;</td>\n";
					print "<td>&nbsp;</td>\n";
					$ln++ ;
				}
			}
			print "</tr>\n";
			last ;
		}
		print "</tr>\n";
		$i++;
	}
	print "</table>\n";
	if ( $jiconnm[0] ne '' )	{
		print "<hr>\n";
		print "<h2>▼常連様専用のアイコンです▼</h2>\n<table cellpadding=5 cellspacing=0 summary=\"常連様専用アイコン\" class=\"joren\">\n";
		$i = 0 ; $j = 0 ;
		while ( 1 )	{
			print "<tr>\n";
			for ( $ln = 1 ; $j <= $#jicon_gif && $ln <= $icon_line ; ) {
				print "<td><img src=\"$jicon_gif[$j]\" alt=\"icon\" width=\"$jicon_gif_w[$j]\" height=\"$jicon_gif_h[$j]\"></td>\n";
				print "<td>$jiconnm[$j]</td>\n";
				$j++ ; $ln++ ;
			}
			if ( $j > $#jicon_gif ) { 
				if ( $ln < $icon_line ) {
					for ( ; $ln <= $icon_line ; ) {
						print "<td>(なし)</td>\n";
						print "<td>(←空席)</td>\n";
						$ln++ ;
					}
				}
				print "</tr>\n";
				last ;
			}
			print "</tr>\n";
			$i++;
		}
		print "</table>\n";
	}
	print "";
	&footer ;															#<<<htmlフッター出力
	exit;
}
###<--------------------------------------------------------------
###<---   エラー処理
###<--------------------------------------------------------------
sub error {
	&header ;
	print "<ul class=\"back\">\n<li><a href=\"$script\">戻る</a></li>\n</ul>\n";
	print "<p class=\"error\">$_[0]</p>\n";
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
			print "<img src=\"$jicon_gif[$k]\" $dmy alt=\"Icon\">";
			last ;
		}
	}
	if ( $found == 0 )	{
		if ( $_[0] eq $oiconnm )	{
			$found = 1 ;
			if ( $oicon_gif_w != 0 ) { $dmy = "width=\"$oicon_gif_w\" height=\"$oicon_gif_h\"" ; } else { $dmy = "" ; }
			print "<img src=\"$oicon_gif\" $dmy alt=\"Icon\">";
		}
	}
	if ( $found == 0 )	{
		if ( !($icon) )	{	$icon = 0 ;	}
		if ( $icon_gif_w[$icon] != 0 ) { $dmy = "width=\"$icon_gif_w[$icon]\" height=\"$icon_gif_h[$icon]\"" ; } else { $dmy = "" ; }
		print "<img src=\"$icon_gif[$icon]\" $dmy alt=\"Icon\">";
	}		
}
###<-------------------------------------------------------------
###<---   ログダウンロードi001112
###<--------------------------------------------------------------
sub download {
    print "Content-type: text/download\n\n";
    print "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\">\n<html lang=\"ja\">\n<head>\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=Shift_JIS\">\n<title>$title</title>\n<style type=\"text/css\">\n<!--\nh1,h2,.adminmessage,.totalcount\n{\ntext-align:center;\n}\n.logdownload ul,.logdownload p\n{\nlist-style:none;\nmargin-left:0;\npadding-left:0;\ntext-align:center;\n}\n-->\n</style>\n</head>\n";
	print "<body>\n";
	&disp ; 
	print "";
	&footer ;
    exit;
}
###<--------------------------------------------------------------
###<---   Information
###<--------------------------------------------------------------
sub info	{	
	&header ;															#<<<htmlヘッダー出力
	print "<ul class=\"back\">\n<li><a href=\"$script\">戻る</a></li>\n</ul>\n";
	print "<h1>&lt;&lt;&lt; \昇\進資格 &gt;&gt;&gt;</h1>\n";
	print "<p class=\"rule\">以下の投稿回数に従って、あなたは\昇\進していきます!!</p>\n";
	$i =  0;
	print "<table cellpadding=5 cellspacing=1 summary=\"昇進資格\" class=\"shoshinshikaku\">\n";
	print "<tr>\n";
	print "<th>資格</th>\n";
	print "<th>投稿回数</th>\n";
	print "<th>アイコン</th>\n";
	print "</tr>\n";
	$k = $#rank ;
	for ( @rank )	{
		print "<tr>\n";
		print "<td>";
		if ( $acs == 0 ) {
			print "$rank[$i]";
		}	else	{
			print "$rankicon[$i]";
		}
		print "</td>\n";
		print "<td>";
		$j = $OIWAI[$i+1] - 1 ;
		if ( $i != $k )	{
			print "$OIWAI[$i]&nbsp;～$j&nbsp;回\n";
		}	else	{
			print "$OIWAI[$i]&nbsp;回以上\n";
		}
		print "</td>\n";
		print "<td><img src=\"$rankicon[$i]\" alt=\"icon\" width=\"$rankicon_w[$i]\" height=\"$rankicon_h[$i]\"></td>\n" if ( $rankicon[$i] ) ;
		print "<td>なし</td>\n" if ( !($rankicon[$i]) ) ;
		print "</tr>\n";
		$i++;
	}
	print "</table>\n";
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
