#! /usr/bin/perl

#���e�v���o�C�_�Ŏw�肵�Ă���p�X���L�q
#
# Xplorer �i�t���[�\�t�g�j
$ver = 1.01;
$Last_Modified = "2002/06/26";
# Copyright (C) 2002 suepon , All rights reserved.
# http://CGIScriptMarket.com/
#
# --------------------------------- �g�p�@ --------------------------------- #
#
# �� ���ɓ���ݒ�͂���܂���B
# �@ ��{�I�ɐݒu�����ꏊ�ȉ��ɂ���S�Ẵt�@�C�����c���[�\���̑ΏۂɂȂ�܂��B
# �� �ݒu�����ɂ��A�ݒu�ꏊ�ƃc���[�\���������K�w���قȂ�ꍇ�́A
# �@ �ݒ蕔�Őݒ���s���ĉ������B
# �� ���K�҂�Macintosh ������ȊO���ɂ���ĕ\������t�H���_�摜�������ύX����̂�
# �@ �t�H���_�摜�͎�����OS�Ɋւ�炸�S�ăA�b�v���[�h���ĉ������B
# �� �摜�t�@�C���̖��O�͓��������ɖ��ڂɊւ���Ă��܂��B
# �@ �Ǝ��̉摜���g�p����ꍇ���A�t�@�C�����̓I���W�i���̖��O���g���ĉ������B
# �� �t���[�����g�p�����A�c���[�\�����������g�p����ꍇ�́A
# �@ Xplorer.cgi?menu �Ƃ����`���ŌĂяo���ĉ������B
#
# �� �ݒu�\���}
#
#    /public_html/
#          ��
#          �� /tree_image/  �A�C�R���摜�ݒu�f�B���N�g��
#          ��      ��
#          ��      �� close_mac.gif
#          ��      �� close_win.gif
#          ��      �� open_mac.gif
#          ��      �� open_win.gif
#          ��      �� home_mac.gif
#          ��      �� home_win.gif
#          ��      �� line0.gif
#          ��      �� line1.gif
#          ��      �� line2.gif
#          ��      �� line3.gif
#          ��      �� text.gif
#          ��      �� doc.gif
#          ��      �� image.gif
#          ��      �� sound.gif
#          ��      �� file.gif
#          ��
#          �� Xplorer.cgi (�p�[�~�b�V�����F705 or 755)
#
# �� ����
# �@ �c���[���j���[�̏����o���ɂ�CGI�A�c���[�̐���ɂ�JavaScript���g���Ă���ׁA
# �@ �c���[��\������܂łɂ̓T�[�o�[�ɕ��S��������A
# �@ �c���[���쎞�ɂ̓��[�J���}�V���ɕ��S��������܂��B
# �@ ���ׁ̈A�c���[�\���Ώۃt�@�C���������܂�ɂ�����������A
# �@ �f�B���N�g���\�������܂�ɂ��[���K�w�ɋy��ł���ꍇ�́A
# �@ ���ꂼ�ꂻ��Ȃ�ɏ������x���Ȃ�܂��B
# �@ �ݒu��͓���󋵂��悭�m�F���A
# �@ �e���ɋɒ[�ȕs��������Ȃ��悤�ɐݒ蕔�Œ������ĉ������B
#
# �@ ���A��L�����l��CGI���g�p����̂́A�c���[�𐶐����鎞�����ł��B
# �@ �Ȃ̂ŁA�c���[�̐����ɉߑ�ȃT�[�o�[���ׂ�������悤�ł���΁A
# �@ ��x�������ꂽ�c���[�̃\�[�X���R�s�[����HTML�t�@�C���Ƃ��Ďg�p���A
# �@ ���e�ɕύX�����������ɍĐ������ăR�s�[����c�ƌ����g��������̎�ł��B
# �@ ���̏ꍇ���A����\���͕K���c���ĉ������B
#
# ----------------------------- �ݒ蕔�������� ----------------------------- #

# ���̃X�N���v�g�t�@�C���̖��O
#�iindex.cgi�ɂ���ƂقƂ�ǂ̃T�[�o�[�Ńf�t�H���g�C���f�b�N�X�Ƃ��ĔF������܂��j
$script = "Xplorer.cgi";

# �c���[�\���J�n�f�B���N�g���𑊑΃p�X�ŋL�q�i"."�ł��̃X�N���v�g�ݒu�ꏊ�ȉ��j
# ��F�Q���document�Ƃ����f�B���N�g������J�n����ꍇ�́A"../../document"
#�i�Ō��/��t���Ȃ����Ɓj
$st_dir = ".";

# �ŏ��ɉE�t���[���ɕ\������y�[�W
#�iXplorer.cgi?def_top �Ƃ���Ƃ��̃X�N���v�g�̃^�C�g�����\������܂��j
$top_page = "./$script?def_top";

# �c���[�̍ŏ㕔�ɕ\�����镶����
# �������N���b�N�����Ƃ��Ƀt���[������������ꍇ��target�����Œ�������
# ���̃X�N���v�g���o�͂���E�t���[���Ftarget=disp
# �t���[�������Ftarget=_top
$home = "<a href='./$script?def_top' target='disp'>�z�[��</a>";

# �c���[�\���t���[���̉���
$frame_cols = 200;

# �c���[���̍��]������
$l_mgn = 0;

# �c���[���̉��s����
$offset_height = 16;

# �摜�ݒu�f�B���N�g��
$img_dir = "./tree_image";

# �C���[�W����
$img_parm = "width=16 height=16 align=absmiddle";

# �y�[�W�^�C�g��(<title></title>)
$page_title = "Xplorer";

# �y�[�W�^�C�g���������o���[�h
# �Ώۃt�@�C����HTML�t�@�C���̏ꍇ�y�[�W�^�C�g�����������o���ăc���[�ɕ\��
# �iHTML�t�@�C���ł�<title>�^�O���ȗ�����Ă���ꍇ�͌��o�ł��܂���j
# on�F1; off�F0;
$anchor_mode = 1;

# �c���[�\���̑ΏۂƂ���t�@�C���̊g���q�i.�͗v��܂���j
# @search_type = (); �Ƃ���΁A�S�Ă̊g���q���ΏۂɂȂ�܂��B
@search_type = ("html","htm","shtml","txt","gif","jpg","jpeg","png","cgi","mid","wav");

# �c���[�\���̑Ώۂ��珜�O����f�B���N�g���̖��O�i���m�ȑ��΃p�X�ŋL�q�j
# �L�q��F@pass_dir = ("./image","./cgi-bin/","./hoge/uhehe"); �i�Ō��/��t���Ȃ����Ɓj
@pass_dir = ("","");

# �c���[�\���̑Ώۂ��珜�O����t�@�C�����i���m�ȑ��΃p�X�ŋL�q�j
# ���̃t�@�C�����̂��w�肵�Ȃ��ƃc���[�\���̑ΏۂɂȂ�܂��B
# �L�q��F@pass_files = ("./index.html","./himitsu/xxx.html","./hoge/uhehe.html");
@pass_files = ("./$script","");

# BODY�ݒ�
$body = '<body text="#000000" bgcolor="#ffffff">';

# STYLE�ݒ�
$style = <<STL;
<style>
body			{ font-size:10pt; }
A				{ text-decoration: none; }
A:link		{ text-decoration: none; color:#0000ff; }
A:visited	{ text-decoration: none; color:#0000ff; }
A:hover		{ text-decoration: underline; color:#ff0000; }
</style>
STL

# Netscape4~ �̓y�[�W�ǂݍ��݌�ɕ\���̈悪�L�����Ă�
# �X�N���[���o�[���o�Ă��Ȃ��̂ŗ\�ߗL����x�̉������m�ۂ��Ă����K�v������܂��B
# �������K�v�ȏꍇ�͂��̒l�𒲐����ĉ������B
#�i���̐ݒ��Netscape4~ �ɑ΂��Ă����K�p����܂���j
$layer_w = 300;

# ----------------------------- �ݒ蕔�����܂� ----------------------------- #

$ver = sprintf("v.%.2f",$ver);
if ($ENV{'HTTP_USER_AGENT'} =~ /mac/i) { $os = "mac"; }
else { $os = "win"; }
if ($ENV{'HTTP_USER_AGENT'} =~ /\[.*?\]/i) { $N4 = 1; }

$buffer = $ENV{'QUERY_STRING'};
if (! $buffer) { &make_frame; }
elsif ($buffer eq 'def_top') { &print_message("Xplorer $ver"); }
elsif ($buffer ne 'menu') { &print_message("�g�p�@���Ԉ���Ă��܂�"); }

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

sub copy {	# ����\�� �폜�֎~

	print "<!----------------------------------------------------\n";
	print "�� Xplorer $ver (Free Soft)                         ��\n";
	print "�� Copyright (C) 2002 suepon , All rights reserved. ��\n";
	print "�� Script found at http://CGIScriptMarket.com/      ��\n";
	print "----------------------------------------------------->\n";
}
