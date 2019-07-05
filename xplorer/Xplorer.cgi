#! /usr/bin/perl

#↑各プロバイダで指定しているパスを記述
#
# Xplorer （フリーソフト）
$ver = 1.01;
$Last_Modified = "2002/06/26";
# Copyright (C) 2002 suepon , All rights reserved.
# http://CGIScriptMarket.com/
#
# --------------------------------- 使用法 --------------------------------- #
#
# ■ 特に難しい設定はありません。
# 　 基本的に設置した場所以下にある全てのファイルがツリー表示の対象になります。
# ■ 設置環境等により、設置場所とツリー表示したい階層が異なる場合は、
# 　 設定部で設定を行って下さい。
# ■ 来訪者がMacintosh かそれ以外かによって表示するフォルダ画像を自動変更するので
# 　 フォルダ画像は自分のOSに関わらず全てアップロードして下さい。
# ■ 画像ファイルの名前は内部処理に密接に関わっています。
# 　 独自の画像を使用する場合も、ファイル名はオリジナルの名前を使って下さい。
# ■ フレームを使用せず、ツリー表示部だけを使用する場合は、
# 　 Xplorer.cgi?menu という形式で呼び出して下さい。
#
# ■ 設置構成図
#
#    /public_html/
#          │
#          ├ /tree_image/  アイコン画像設置ディレクトリ
#          │      │
#          │      ├ close_mac.gif
#          │      ├ close_win.gif
#          │      ├ open_mac.gif
#          │      ├ open_win.gif
#          │      ├ home_mac.gif
#          │      ├ home_win.gif
#          │      ├ line0.gif
#          │      ├ line1.gif
#          │      ├ line2.gif
#          │      ├ line3.gif
#          │      ├ text.gif
#          │      ├ doc.gif
#          │      ├ image.gif
#          │      ├ sound.gif
#          │      └ file.gif
#          │
#          └ Xplorer.cgi (パーミッション：705 or 755)
#
# ■ 注意
# 　 ツリーメニューの書き出しにはCGI、ツリーの制御にはJavaScriptを使っている為、
# 　 ツリーを表示するまでにはサーバーに負担がかかり、
# 　 ツリー操作時にはローカルマシンに負担がかかります。
# 　 その為、ツリー表示対象ファイル数があまりにも多かったり、
# 　 ディレクトリ構成があまりにも深い階層に及んでいる場合は、
# 　 それぞれそれなりに処理が遅くなります。
# 　 設置後は動作状況をよく確認し、
# 　 各環境に極端な不可がかからないように設定部で調整して下さい。
#
# 　 又、上記した様にCGIを使用するのは、ツリーを生成する時だけです。
# 　 なので、ツリーの生成に過大なサーバー負荷をかけるようであれば、
# 　 一度生成されたツリーのソースをコピーしてHTMLファイルとして使用し、
# 　 内容に変更があった時に再生成してコピーする…と言う使い方も一つの手です。
# 　 その場合も、著作表示は必ず残して下さい。
#
# ----------------------------- 設定部ここから ----------------------------- #

# このスクリプトファイルの名前
#（index.cgiにするとほとんどのサーバーでデフォルトインデックスとして認識されます）
$script = "Xplorer.cgi";

# ツリー表示開始ディレクトリを相対パスで記述（"."でこのスクリプト設置場所以下）
# 例：２つ上のdocumentというディレクトリから開始する場合は、"../../document"
#（最後に/を付けないこと）
$st_dir = ".";

# 最初に右フレームに表示するページ
#（Xplorer.cgi?def_top とするとこのスクリプトのタイトルが表示されます）
$top_page = "./$script?def_top";

# ツリーの最上部に表示する文字列
# ここをクリックしたときにフレームを解除する場合はtarget属性で調整する
# このスクリプトが出力する右フレーム：target=disp
# フレーム解除：target=_top
$home = "<a href='./$script?def_top' target='disp'>ホーム</a>";

# ツリー表示フレームの横幅
$frame_cols = 200;

# ツリー部の左余白調整
$l_mgn = 0;

# ツリー部の改行調整
$offset_height = 16;

# 画像設置ディレクトリ
$img_dir = "./tree_image";

# イメージ属性
$img_parm = "width=16 height=16 align=absmiddle";

# ページタイトル(<title></title>)
$page_title = "Xplorer";

# ページタイトル自動検出モード
# 対象ファイルがHTMLファイルの場合ページタイトルを自動検出してツリーに表示
# （HTMLファイルでも<title>タグが省略されている場合は検出できません）
# on：1; off：0;
$anchor_mode = 1;

# ツリー表示の対象とするファイルの拡張子（.は要りません）
# @search_type = (); とすれば、全ての拡張子が対象になります。
@search_type = ("html","htm","shtml","txt","gif","jpg","jpeg","png","cgi","mid","wav");

# ツリー表示の対象から除外するディレクトリの名前（正確な相対パスで記述）
# 記述例：@pass_dir = ("./image","./cgi-bin/","./hoge/uhehe"); （最後に/を付けないこと）
@pass_dir = ("","");

# ツリー表示の対象から除外するファイル名（正確な相対パスで記述）
# このファイル自体も指定しないとツリー表示の対象になります。
# 記述例：@pass_files = ("./index.html","./himitsu/xxx.html","./hoge/uhehe.html");
@pass_files = ("./$script","");

# BODY設定
$body = '<body text="#000000" bgcolor="#ffffff">';

# STYLE設定
$style = <<STL;
<style>
body			{ font-size:10pt; }
A				{ text-decoration: none; }
A:link		{ text-decoration: none; color:#0000ff; }
A:visited	{ text-decoration: none; color:#0000ff; }
A:hover		{ text-decoration: underline; color:#ff0000; }
</style>
STL

# Netscape4~ はページ読み込み後に表示領域が広がっても
# スクロールバーが出てこないので予め有る程度の横幅を確保しておく必要があります。
# 調整が必要な場合はこの値を調整して下さい。
#（この設定はNetscape4~ に対してしか適用されません）
$layer_w = 300;

# ----------------------------- 設定部ここまで ----------------------------- #

$ver = sprintf("v.%.2f",$ver);
if ($ENV{'HTTP_USER_AGENT'} =~ /mac/i) { $os = "mac"; }
else { $os = "win"; }
if ($ENV{'HTTP_USER_AGENT'} =~ /\[.*?\]/i) { $N4 = 1; }

$buffer = $ENV{'QUERY_STRING'};
if (! $buffer) { &make_frame; }
elsif ($buffer eq 'def_top') { &print_message("Xplorer $ver"); }
elsif ($buffer ne 'menu') { &print_message("使用法が間違っています"); }

&open_dir($st_dir);

$i = 0;
foreach $list (@lists) {
	if (! ($_ =~ /\.\w/)) {
		@plus = &open_dir($list);
		if (@plus) {
			$values = $#lists;
			$now = $i + 1;
			$p = @plus;
			for ($ii = $values; $ii >= $now; $ii --) {
				$lists[$ii + $p] = $lists[$ii];
			}
			foreach $new (@plus) {
				$lists[$now] = $new;
				$now ++;
			}
		}
	}
	$i ++;
}

print "Content-type:text/html\n\n";
&copy;
print "<html>\n<head>\n<title>$page_title</title>\n$style<script>\n";

print <<EOF;
img_close = new Image();
img_close.src = "$img_dir/close_$os\.gif";
img_open = new Image();
img_open.src = "$img_dir/open_$os\.gif";

N4 = IE = N6 = 0;
if (document.layers) N4 = 1;
else if (document.all) IE = 1;
else if (document.getElementById) N6 = 1;

function menu_open(p) {
	if (! cmv[p]) cmv[p] = new Array();
	if (N4) {
		p = eval(this.name.replace("menu",""));
		doc = document.layers["menu" + p];
		dis = doc.document.images["pos" + p];
		if (! dis) return;
		offY = doc.pageY;
	}
	else dis = document.images["pos" + p];
	if (IE) {
		doc = document.all("menu" + p);
		offY = doc.style.posTop;
	}
	if (N6) {
		doc = document.getElementById("menu" + p);
		offY = parseInt(doc.style.top);
	}
	if (dis.src.indexOf("close") > -1) {
		dis.src = img_open.src;
		for (i in cmv[p]) {
			offY += 16;
			if (N4) doc = document.layers["menu" + cmv[p][i]];
			if (IE) doc = document.all("menu" + cmv[p][i]).style;
			if (N6) doc = document.getElementById("menu" + cmv[p][i]).style;
			with (doc) {
				visibility = vis;
				top = offY;
			}
		}
	}
	else {
		end = cmv[p];
		limit = 0;
		dis.src = img_close.src;
		if (end) {
			for (i in cmv[p]) if (cmv[cmv[p][i]]) end = end.concat(cmv[cmv[p][i]]);
			if (cmv[end[end.length-1]]) end = end.concat(cmv[end[end.length-1]]);
			for (i = 0; i < end.length; i++)
				if (end[i]) limit = Math.max(limit,end[i]);
			for (i = p+1; i <= limit; i++) {
				if (N4) {
					doc = document.layers["menu" + i];
					dis = doc.document.images["pos" + i];
				}
				else dis = document.images["pos" + i];
				if (IE) doc = document.all("menu" + i).style;
				if (N6) doc = document.getElementById("menu" + i).style;
				if (dis) dis.src = img_close.src;
				doc.visibility = "hidden";
				doc.top = 0;
			}
		}
	}
	if (cmv[p]) {
		for (i = eval(cmv[p][cmv[p].length-1]) + 1; i < list; i++) {
			if (N4) doc = document.layers["menu" + i];
			if (IE) doc = document.all("menu" + i).style;
			if (N6) doc = document.getElementById("menu" + i).style;
			if (doc.visibility == vis) {
				offY += 16;
				doc.top = offY;
			}
		}
	}
}

function init() {
	if (N4) { defY = offY = document.layers["menu0"].pageY; vis = "show"; }
	else { defY = offY = $offset_height; vis = "visible"; }

	for (i in def) {
		if (N4) doc = document.layers["menu" + def[i]];
		if (IE) doc = document.all("menu" + def[i]).style;
		if (N6) doc = document.getElementById("menu" + def[i]).style;
		with (doc) {
			visibility = vis;
			top = offY;
		}
		offY += $offset_height;
	}

	if (document.layers) {
		for (i = 0; i < list; i ++) {
			doc = document.layers["menu" + i];
			doc.captureEvents(Event.MOUSEDOWN);
			doc.onmousedown = menu_open;
		}
	}
}

window.onload = init;
</script>
</head>
$body
<tt><nobr>
EOF

&make_layer('',$home);
$total = 0;
foreach (@lists) {

	$name = "";
	if ($anchor_mode && $_ =~ /\.s?htm/i) {
		open (HTML,$_);
		@html = <HTML>;
		foreach $v (@html) {
			if ($v =~ /(<title>)(.*?)<\/title>/i) { $name = $2; last; }
		}
		close (HTML);
		$name =~ s/[\,\"]//g;
	}
	if (! $name) { $name = substr($_,rindex($_,"/") + 1,length($_) - (rindex($_,"/") + 1)); }

	$dir = substr($_,0,rindex($_,"/"));
	if ($dir eq $st_dir) { $dir = "$st_dir/$name"; }
	if (! ($_ =~ /\.\w/)) { $parent{"$dir/$name"} = $total; }

	if ($parent{$dir} eq '') {
		$parent{$dir} = $class = $total;
	}
	else { $class = $parent{$dir}; }

	if ($class == $total) { $class = ''; }
	if ($_ =~ /\.\w/) { $anchor = "$_"; }
	else { $anchor = ""; }

	if ($class{$_} eq 'def') { $def .= "\,'$total'"; }
	if ($class ne '') { $cmv{$class} .= "\,'$total'"; }

	$bd = $bd{$_};
	&make_layer($total,$name,$anchor);
	$total ++;
}

print "</nobr></tt>\n";
print "<script>\n";

$def =~ s/\,//;
print "list = $total;\n";
print "def = new Array(''\,$def);\n";
print "cmv = new Array();\n";

while (($key,$value) = each %cmv) {
	$value =~ s/\,//;
	print "cmv\[$key\] = new Array($value);\n";
}

print "</script>\n";
print "</body>\n</html>\n";

exit;

sub open_dir {

	@new1 = ();
	@new2 = ();
	$dir = "$_[0]/";

	opendir DIR,$dir;
	@dir_value = readdir DIR;
	close (DIR);

	foreach $value (@dir_value) {
		if (! ($value =~ /\./)) {
			$c = 0;
			foreach $pass_d (@pass_dir) {
				if ("$dir$value" eq $pass_d) { $c ++; }
			}
			if ($c == 0) {
				push (@new1,"$dir$value");
				if (! $par) { $class{"$dir$value"} = 'def'; }
				$bd = $bd{$_[0]};
				$bd =~ s/1/2/g;
				$bd =~ s/3/0/g;
				$bd{"$dir$value"} = $bd . "1";
			}
		}
		else {
			$c1 = $c2 = 0;
			if (! @search_type) {
					if ($value =~ /\.\w/) {
						$c1 = 1;
						foreach $pass_f (@pass_files) {
							if ($pass_f eq "$dir$value") { $c2 ++; }
						}
					}
			}
			else {
				foreach $type (@search_type) {
					if ($value =~ /\.$type/i) {
						$c1 = 1;
						foreach $pass_f (@pass_files) {
							if ($pass_f eq "$dir$value") { $c2 ++; }
						}
					}
				}
			}
			if ($c1 > 0 && $c2 == 0) {
				push (@new2,"$dir$value");
				if (! $par) { $class{"$dir$value"} = 'def'; }
				$bd = $bd{$_[0]};
				$bd =~ s/1/2/g;
				$bd =~ s/3/0/g;
				$bd{"$dir$value"} = $bd . "1";
			}
		}
	}
	@new1 = sort @new1;
	@new2 = sort @new2;
	push (@new1,@new2);
	$bd{$new1[$#new1]} =~ s/1/3/;
	$par ++;
	if ($_[0] eq $st_dir) { push (@lists,@new1); }
	else { return @new1; }
}

sub make_layer {

	$ivent = "";
	if ($_[1] eq $home) {
		$bd = "";
		$_[1] = "<img src='$img_dir/home_$os\.gif' $img_parm> $_[1]";
	}
	elsif ($_[2]) {
		if ($_[2] =~ /\.(gif|jpg|jpeg|png|bmp)/) { $img = "image\.gif"; }
		elsif ($_[2] =~ /\.s?htm/) { $img = "doc\.gif"; }
		elsif ($_[2] =~ /\.(txt|cgi|pl|dat|log)/) { $img = "text\.gif"; }
		elsif ($_[2] =~ /\.(mid|wav|avi|mp|ra|swf|asf)/) { $img = "sound\.gif"; }
		else { $img = "file\.gif"; }
		$_[1] = "<img src='$img_dir/$img' $img_parm> <a href='$_[2]' target='disp'>$_[1]</a>";
	}
	elsif ($N4) {
		$_[1] = "<img name=pos$_[0] src='$img_dir/close_$os\.gif' $img_parm> $_[1]";
	}
	else {
		$ivent = " onClick='menu_open($_[0])'";
		$_[1] = "<img name=pos$_[0] src='$img_dir/close_$os\.gif' $img_parm> $_[1]";
	}
	$bd =~ s/(\d)/<img src='$img_dir\/line$1\.gif' $img_parm>/g;
	if ($N4) {
		$hei = int(@lists * $offset_height / 4);
		print "<layer name=menu$_[0] width=$layer_w height=$hei left=$l_mgn visibility=hidden>&nbsp$bd$_[1]</layer><br>\n";
	}
	else {
		print "<div id=menu$_[0]$ivent style='position:absolute; left:$l_mgn","px; visibility:hidden;'>&nbsp$bd$_[1]</div>\n";
	}
}

sub make_frame {

	print "Content-type:text/html\n\n";
	&copy;
	print "<html>\n<head>\n<title>$page_title</title>\n</head>\n";
	print "<frameset cols=\"$frame_cols,*\">\n";
	print "<frame src=\"$script?menu\" scrolling=auto>\n";
	print "<frame src=\"$top_page\" name=\"disp\">\n";
	print "</frameset>\n";
	print "</html>\n";

	exit;
}

sub print_message {

	print "Content-type:text/html\n\n";
	print "<h2 align=center><br>$_[0]</h2>\n";

	exit;
}

sub copy {	# 著作表示 削除禁止

	print "<!----------------------------------------------------\n";
	print "□ Xplorer $ver (Free Soft)                         □\n";
	print "□ Copyright (C) 2002 suepon , All rights reserved. □\n";
	print "□ Script found at http://CGIScriptMarket.com/      □\n";
	print "----------------------------------------------------->\n";
}
