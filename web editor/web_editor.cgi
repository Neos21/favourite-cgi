#! /usr/bin/perl

#���e�v���o�C�_�Ŏw�肵�Ă���p�X���L�q
#
# WEB EDITOR �i�t���[�\�t�g�j
$ver = 2.01;
$Last_Modified = "2002/12/04";
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
# �� �f�B���N�g���̃p�[�~�b�V�����ݒ肪�����Ɏw�肳��Ă���T�[�o�[�ł́A
# �@ ���̃X�N���v�g���g���Ȃ��ꍇ������܂��B
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
#          �� web_editor.cgi (�p�[�~�b�V�����F705 or 755)
#          �� jcode.pl
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
# ----------------------------- �ݒ蕔�������� ----------------------------- #

# �p�X���[�h
$passwd = "admin";

# ���̃X�N���v�g�t�@�C���̖��O
$script = "web_editor.cgi";

# �c���[�\���J�n�f�B���N�g���𑊑΃p�X�ŋL�q�i"."�ł��̃X�N���v�g�ݒu�ꏊ�ȉ��j
# ��F�Q���document�Ƃ����f�B���N�g������J�n����ꍇ�́A"../../document"
#�i�Ō��/��t���Ȃ����Ɓj
$st_dir = ".";

# �c���[�\���t���[���̉���
$frame_cols = 150;

# �c���[���̍��]������
$l_mgn = 0;

# �c���[���̉��s����
$offset_height = 16;

# �摜�ݒu�f�B���N�g��
$img_dir = "./tree_image";

# �C���[�W����
$img_parm = "width=16 height=16 align=absmiddle";

# �y�[�W�^�C�g���������o���[�h
# �Ώۃt�@�C����HTML�t�@�C���̏ꍇ�y�[�W�^�C�g�����������o���ăc���[�ɕ\��
# �iHTML�t�@�C���ł�<title>�^�O���ȗ�����Ă���ꍇ�͌��o�ł��܂���j
# on�F1; off�F0;
$anchor_mode = 0;

# �c���[�\���̑ΏۂƂ���t�@�C���̊g���q�i.�͗v��܂���j
# EX. @search_type = ("html","htm","shtml","txt","cgi","dat","log","csv");
# EX. @search_type = (); �Ƃ���΁A�S�Ă̊g���q���ΏۂɂȂ�܂��B
@search_type = ();

# �e�L�X�g�����ɂ��Ȃ��t�@�C���̊g���q�i����ȊO�̓t�@�C�����e�̕ҏW���\�ɂȂ�܂��j
@no_text_type = ("gif","jpg","jpeg","png","mid","mp3","wav","mpg","mpeg","bmp","pdf");

# �c���[�\���̑Ώۂ��珜�O����f�B���N�g���̖��O�i���m�ȑ��΃p�X�ŋL�q�j
# �L�q��F@pass_dir = ("./image","./cgi-bin/","./hoge/uhehe"); �i�Ō��/��t���Ȃ����Ɓj
# EX. @pass_dir = (); �Ƃ���΁A�S�Ẵf�B���N�g�����ΏۂɂȂ�܂��B
@pass_dir = ();

# �c���[�\���̑Ώۂ��珜�O����t�@�C�����i���m�ȑ��΃p�X�ŋL�q�j
# ���̃t�@�C�����̂��w�肵�Ȃ��ƃc���[�\���̑ΏۂɂȂ�܂��B
# �L�q��F@pass_files = ("./index.html","./himitsu/xxx.html","./hoge/uhehe.html");
@pass_files = ("./$script","");

# BODY�ݒ�
$body = '<body text="#000000" bgcolor="#ffffff">';

# STYLE�ݒ�1 �i�c���[�\�����j
$style1 = <<STL;
<style>
body        { font-size:10pt; }
A           { text-decoration: none; }
A:link      { text-decoration: none; color:#0000ff; }
A:visited   { text-decoration: none; color:#0000ff; }
A:hover     { text-decoration: underline; color:#ff0000; }
</style>
STL

# STYLE�ݒ�2 �i�ҏW��ʁj
$style2 = <<STL;
<style>
body,td,tt  { font-size:10pt; }
h2          { font-size:20pt; }
A           { text-decoration: none; }
A:link      { text-decoration: none; color:#0000ff; }
A:visited   { text-decoration: none; color:#0000ff; }
A:hover     { text-decoration: underline; color:#ff0000; }
</style>
STL

# Netscape4~ �̓y�[�W�ǂݍ��݌�ɕ\���̈悪�L�����Ă�
# �X�N���[���o�[���o�Ă��Ȃ��̂ŗ\�ߗL����x�̉������m�ۂ��Ă����K�v������܂��B
# �������K�v�ȏꍇ�͂��̒l�𒲐����ĉ������B
#�i���̐ݒ��Netscape4~ �ɑ΂��Ă����K�p����܂���j
$layer_w = 300;

# ----------------------------- �ݒ蕔�����܂� ----------------------------- #

require "jcode.pl";
$ver = sprintf("v.%.2f",$ver);
if ($ENV{'HTTP_USER_AGENT'} =~ /mac/i) { $os = "mac"; }
else { $os = "win"; }
if ($ENV{'HTTP_USER_AGENT'} =~ /\[.*?\]/i) { $N4 = 1; }
%charset = ('jis' => 'iso-2022-jp','sjis' => 'Shift_JIS','euc' => 'euc-jp');
@parm = (600,604,644,606,666,700,705,755,777);
@jpwd = ('�t�@�C����','�����R�[�h','�p�[�~�b�V����','  �m�@�F  ','  �ہ@��  ','���Z�b�g','���̃t�@�C�����폜����','�f�B���N�g�����ƍ폜����','�t�@�C���A�b�v���[�_','���ݕҏW���̃t�@�C���́A�u���E�U�Ŋm�F���邱�Ƃ��o���܂���','�t�@�C��','�f�B���N�g��','���폜���܂��A��낵���ł����H','�����L��܂���');
$home = "<a href='./$script?in' target='disp'>WEB EDITOR</a>";

if ($ENV{'REQUEST_METHOD'} eq 'POST') {
   binmode (STDIN);
   read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
   @pairs = split(/Content-Disposition/i,$buffer);
   foreach (@pairs) {
      $key = "";
      if ($_ =~ /Content-Type\:.*?[\r\n|\r|\n]{4}/i) {
         ($a,$value) = split (/Content-Type\:.*?[\r\n|\r|\n]{4}/,$_);
         ($a,$name,$b,$filename,$c) = split (/\"/,$_);
         if ($filename =~ /\\/) { $key = "\\"; }
         elsif ($filename =~ /\//) { $key = "\/"; }
         if ($key) { $filename = substr ($filename,rindex ($filename,$key) + 1,length ($filename)); }
         $in{'filename'} = $filename;
      }
      else {
         if ($_ =~ /name\=\"(.*?)\"/) { $name = $1; $value = $_; }
         $value =~ s/.*?[\r\n|\r|\n]{4}//;
      }
      ($value,$a) = split (/[\r\n|\r|\n]{2}\-{29}/,$value);
      if ($name eq 'file' && $filename) { $file{$filename} = $value; }
      else {
         $value =~ s/\r\n/\n/g;
         $value =~ s/\r/\n/g;
         $in{$name} = $value;
      }
   }
}
else {
   $buffer = $ENV{'QUERY_STRING'};
   @buf = split(/&/,$buffer);
   foreach (@buf) {
      ($name,$value) = split(/=/,$_);
      $value =~ tr/+/ /;
      $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C",hex($1))/eg;
      $in{$name} = $value;
   }
}

$ref = $ENV{'HTTP_REFERER'};

if ($in{'uploader'}) { &uploader; }
elsif ($in{'upload'}) { &upload; }
elsif ($in{'delete'}) { &delete; }
elsif ($in{'deldir'}) { &deldir; }
elsif ($in{'mode'} eq 'edit') { &edit; }
elsif ($buffer eq 'in' || $in{'f_name'} || $in{'in'}) { &in; }
elsif ($in{'pass'} eq $passwd) { &make_frame; }
elsif ($buffer ne 'menu' && $in{'pass'} ne $passwd) { &gate; }
elsif ($buffer ne 'menu') { &print_message("�g�p�@���Ԉ���Ă��܂�"); }

if (! ($ref =~ /$script/)) { print "Location:$script\n\n"; }

&open_dir($st_dir);

$i = 0;
foreach $list (@lists) {
   $f_type = (stat($list))[2];
   $f_type = substr((sprintf ("%03o",$f_type)),0,2);
   if ($f_type == 40) {
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

print "Content-type:text/html; charset=Shift_JIS\n";
print "Pragma:no-cache\n";
print "Cache-Control:no-cache\n";
print "Expires:Thu, 01 Dec 1994 16:00:00 GMT\n\n";
&copy;
print "<html>\n<head>\n<title>WEB EDITOR</title>\n$style1<script>\n";

print <<EOF;
img_close = new Image();
img_close.src = "$img_dir/close_$os\.gif";
img_open = new Image();
img_open.src = "$img_dir/open_$os\.gif";

N4 = IE = N6 = 0;
if (document.layers) N4 = 1;
else if (document.all) IE = 1;
else if (document.getElementById) N6 = 1;
dirname = new Array();

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
      if (String(parent.disp.document.location).match(/$script/)) {
         parent.disp.document.forms[0].dir.value = dirname[p];
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
      if (String(parent.disp.document.location).match(/$script/)) {
         val = dirname[p];
         val = val.substring(0,val.lastIndexOf('/'));
         parent.disp.document.forms[0].dir.value = val;
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

   $f_type = (stat($_))[2];
   $f_type = substr((sprintf ("%03o",$f_type)),0,2);
   $name = substr($_,rindex($_,"/") + 1,length($_) - (rindex($_,"/") + 1));
   $dir = substr($_,0,rindex($_,"/"));
   push (@dirname,"$dir/$name");
   if ($dir eq $st_dir) { $dir = "$st_dir/$name"; }
   if (! ($_ =~ /\.\w/)) { $parent{"$dir/$name"} = $total; }

   if ($parent{$dir} eq '') {
      $parent{$dir} = $class = $total;
   }
   else { $class = $parent{$dir}; }

   if ($class == $total) { $class = ''; }
   if ($f_type != 40) { $anchor = "$_"; }
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

$pa = 0;
foreach (@dirname) {
   $_ =~ s/\.\///g;
   if (! ($_ =~ /\./) && ! $check{$_}) {
      print "dirname\[$pa\] = './$_';\n";
      $check{$_} ++;
   }
   $pa ++;
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
      $_[1] = "<img src='$img_dir/$img' $img_parm> <a href='./$script?f_name=$_[2]' target='disp'>$_[1]</a>";
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

sub in {

   if (! ($ref =~ /$script/)) { print "Location:$script\n\n"; }

   if ($in{'f_name'}) {
      foreach (@no_text_type) {
         if ($in{'f_name'} =~ /$_/i) { &no_text; }
      }

      open (FILE,$in{'f_name'});
      while (<FILE>) { $text .= $_; }
      close (FILE);
      $char = &jcode'getcode(*text);
      $text =~ s/</&lt;/g;
      $text =~ s/>/&gt;/g;
      if ($charset{$char}) { $charset = $charset{$char}; }
      else { $char = "sjis"; $charset = "Shift_JIS"; }
      ($parm,$size) = (stat("$in{'f_name'}"))[2,7];
      $parm = substr((sprintf ("%03o",$parm)),-3);
      $k_size = sprintf ("%.2f",$size / 1000);
      $size = "<tt>&nbsp;$k_size kb ($size bytes)</tt>";
      foreach (@jpwd) { &jcode'convert(*_,$char); }
   }
   else { $size = "<small>�i�C�ӂ̃t�@�C��������͂���ƐV�K�쐬�ɂȂ�܂��j</small>"; }
   if (! $charset) { $charset = "Shift_JIS"; }

   print "Content-type:text/html; charset=$charset{$char}\n";
   print "Pragma:no-cache\n";
   print "Cache-Control:no-cache\n";
   print "Expires:Thu, 01 Dec 1994 16:00:00 GMT\n\n";
   print "<html>\n<head>\n<title>WEB EDITOR</title>\n$style2";
   print "<script>\nfunction doc_check() {\n";
   print "\tif (document.forms[0].f_name.value.match(/\\.(s?html?|txt)/i)) {\n";
   print "\t\tval = document.forms[0].text.value;\n";
   print "\t\tcheck_win = window.open('','check_win','scrollbars,resizable,toolbar,menubar,location,directories,status');\n";
   print "\t\twith (check_win.document) {\n\t\t\topen();\n\t\t\twrite(val);\n\t\t\tclose();\n";
   print "\t\t}\n\t}\n\telse { alert('$jpwd[9]'); }\n}\n";
   print "function del_check(n) {\n\tif (n == 1) {\n\t\tobj = '$jpwd[10]';\n";
   print "\t\tf_name = document.forms[0].f_name.value;\n\t}\n";
   print "\tif (n == 2) {\n\t\tobj = '$jpwd[11]';\n";
   print "\t\tf_name = document.forms[0].dir.value;\n\t}\n";
   print "\tif (f_name && confirm(obj + ' ' + f_name + ' $jpwd[12]'))\n";
   print "\t\treturn true;\n\telse if (f_name) return false;\n";
   print "\telse {\n\t\talert(obj + '$jpwd[13]');\n\t\treturn false;\n\t}\n}\n";

   if ($reflesh == 1) {
      print "parent.menu.location.reload(true)\n";
   }
   print "</script>\n</head>\n<body>\n";
   print "<h2>WEB EDITOR</h2>\n";
   print "<form action='$script' method=post enctype='multipart/form-data'>\n";
   print "<input type=submit name=uploader value='$jpwd[8]'><hr>\n";
   print "<input type=hidden name=mode value=edit>\n";
   print "<table>\n";
   print "<tr><td>$jpwd[0]</td><td><input name=f_name value='$in{'f_name'}' size=40>$size</td></tr>\n";
   print "<tr><td>$jpwd[1]</td><td><select name=char>\n";
   while (($key,$value) = each %charset) {
      if ($char eq $key) { print "<option value='$key' selected>$value\n"; }
      else { print "<option value='$key'>$value\n"; }
   }
   print "</td></tr>\n";
   print "<tr><td>$jpwd[2]</td><td><select name=parm>\n";
   foreach (@parm) {
      if ((! $in{'f_name'} && $_ == 644) || $_ eq $parm) {
         print "<option value='$_' selected>$_\n";
      }
      else { print "<option value='$_'>$_\n"; }
   }
   print "</select></td></tr>\n";
   print "</table>\n";
   print "<textarea name=text cols=80 rows=25 wrap=off>$text</textarea>\n<hr>\n";
   print "<input type=button onClick='doc_check()' value='$jpwd[3]'>\n";
   print "&nbsp;<input type=submit value='$jpwd[4]'>\n";
   print "&nbsp;<input type=reset value='$jpwd[5]'>\n";
   if ($in{'f_name'}) {
      print "&nbsp;&nbsp;&nbsp;<input type=submit onClick='return del_check(1)' name=delete value='$jpwd[6]'>\n";
   }
   print "<p><hr><p>\n";
   print "$jpwd[11]&nbsp;<input name=dir size=40><p>\n";
   print "<input type=submit name=deldir onClick='return del_check(2)' value='$jpwd[7]'>\n";
   print "</form>\n</body>\n</html>\n";

   exit;
}

sub no_text {

   if (! ($ref =~ /$script/)) { print "Location:$script\n\n"; }

   $size = (stat("$in{'f_name'}"))[2];
   $k_size = sprintf ("%.2f",$size / 1000);
   $size = "<tt>&nbsp;$k_size kb ($size bytes)</tt>";

   print "Content-type:text/html; charset=Shift_JIS\n";
   print "Pragma:no-cache\n";
   print "Cache-Control:no-cache\n";
   print "Expires:Thu, 01 Dec 1994 16:00:00 GMT\n\n";
   print "<html>\n<head>\n<title>WEB EDITOR</title>\n$style2";
   print "<script>\nfunction del_check() {\n f_name = document.forms[0].f_name2.value;\n";
   print "\tif (confirm(f_name + '���폜���܂��A��낵���ł����H'))\n";
   print "\t\treturn true;\n\telse return false;\n";
   print "}\n";
   print "</script>\n</head>\n<body>\n";
   print "<h2>WEB EDITOR</h2>\n";
   print "<form action='$script' method=post enctype='multipart/form-data'>\n";
   print "<input type=submit name=in value='�t�@�C���̕ҏW'>&nbsp;";
   print "<input type=submit name=uploader value='�t�@�C���A�b�v���[�_'><hr><p>\n";
   print "<a href='$in{'f_name'}' target=_blank>$in{'f_name'}</a>&nbsp;$size<p>\n";
   print "<input type=hidden name=f_name2 value='$in{'f_name'}'>\n";
   print "<input type=submit name=delete onClick='return del_check()' value='���̃t�@�C�����폜'>\n";
   print "</form>\n</body>\n</html>\n";

   exit;
}

sub uploader {

   if (! ($ref =~ /$script/)) { print "Location:$script\n\n"; }
   if (! $in{'up_val'}) { $in{'up_val'} = 5; }

   print "Content-type:text/html; charset=Shift_JIS\n";
   print "Pragma:no-cache\n";
   print "Cache-Control:no-cache\n";
   print "Expires:Thu, 01 Dec 1994 16:00:00 GMT\n\n";
   print "<html>\n<head>\n<title>WEB EDITOR</title>\n$style2<script>\n";
   print "function up_val_change(p) {\n";
   print "\tval = p.options[p.selectedIndex].value;\n";
   print "\tdocument.location = '$script?uploader=1&up_val=' + val;\n}\n";
   if ($reflesh == 1) {
      print "parent.menu.location.reload(true)\n";
   }
   print "</script>\n</head>\n<body>\n";
   print "<h2>WEB EDITOR</h2>\n";
   print "<form action='$script' method=post enctype='multipart/form-data'>\n";
   print "<input type=submit name=in value='�t�@�C���̕ҏW'><hr>\n";
   print "�A�b�v���[�h��F<input name=dir size=40><br>\n";
   print "�i���t���[���̃f�B���N�g���A�C�R�����N���b�N����ƑI���ł��܂�/�󔒁��ŏ�ʊK�w�j<p>\n";
   print "��x�ɃA�b�v���[�h�ł��鐔�F<select name=up_val onChange='up_val_change(this)'>\n";
   for ($i = 5; $i <= 30; $i += 5) {
      if ($i == $in{'up_val'}) { print "<option value=$i selected>$i\n"; }
      else { print "<option value=$i>$i\n"; }
   }
   print "</select><p>\n";
   print "<table cellpadding=0 cellspacing=0>\n";
   foreach (1..$in{'up_val'}) { print "<tr><td>�t�@�C��</td><td align=right>$_�F</td><td><input type=file name=file size=50></td></tr>\n"; }
   print "</table>\n";
   print "<p><input type=submit name=upload value='  �A�b�v���[�h  '>&nbsp;\n";
   print "<input type=reset value='���Z�b�g'>\n";
   print "</form>\n";
   print "</body></html>\n";

   exit;
}

sub edit {

   if (! ($ref =~ /$script/)) { print "Location:$script\n\n"; }
   if (! $in{'f_name'}) { &print_message("�t�@�C���������L���ł�"); }
   if (! $in{'text'}) { &print_message("�t�@�C�����e���󔒂ł�"); }

   if (! (-e $in{'f_name'})) { $reflesh = 1; }
   $check_dir = substr($in{'f_name'},0,rindex($in{'f_name'},"/"));
   if (! -e $check_dir) {
      @newdir = split(/\//,$check_dir);
      foreach (@newdir) {
         if (! -e "$newdir$_") { mkdir("$newdir$_",0755); }
         $newdir .= "$_/";
      }
   }

   $new = $in{'text'};
   $new =~ s/&lt;/</g;
   $new =~ s/&gt;/>/g;
   if ($in{'char'} ne 'jis' && $in{'char'} ne 'sjis' && $in{'char'} ne 'euc') {
      $in{'char'} = "sjis";
   }
   &jcode'convert(*new,$in{'char'});
   chmod 0666,"$in{'f_name'}";
   open (FILE,"> $in{'f_name'}");
   print FILE $new;
   close (FILE);
   if ($in{'parm'} == 600) { chmod 0600,"$in{'f_name'}"; }
   if ($in{'parm'} == 604) { chmod 0604,"$in{'f_name'}"; }
   if ($in{'parm'} == 644) { chmod 0644,"$in{'f_name'}"; }
   if ($in{'parm'} == 606) { chmod 0606,"$in{'f_name'}"; }
   if ($in{'parm'} == 666) { chmod 0666,"$in{'f_name'}"; }
   if ($in{'parm'} == 700) { chmod 0700,"$in{'f_name'}"; }
   if ($in{'parm'} == 705) { chmod 0705,"$in{'f_name'}"; }
   if ($in{'parm'} == 755) { chmod 0755,"$in{'f_name'}"; }
   if ($in{'parm'} == 777) { chmod 0777,"$in{'f_name'}"; }

   &in;
}

sub upload {

   if (! ($ref =~ /$script/)) { print "Location:$script\n\n"; }
   if (! %file) { &uploader; }
   if (! $in{'dir'}) { $in{'dir'} = $st_dir; }

   print "Content-type:text/html; charset=Shift_JIS\n";
   print "Pragma:no-cache\n";
   print "Cache-Control:no-cache\n";
   print "Expires:Thu, 01 Dec 1994 16:00:00 GMT\n\n";
   print "<html>\n<head>\n<title>WEB EDITOR</title>\n$style2";
   print "<script>parent.menu.location.reload(true)</script>\n";
   print "</head>\n<body>\n";
   print "<h2>WEB EDITOR</h2>\n";
   print "<form action='$script' method=post enctype='multipart/form-data'>\n";
   print "<input type=submit name=in value='�t�@�C���̕ҏW'>&nbsp;";
   print "<input type=submit name=uploader value='�t�@�C���A�b�v���[�_'><hr>\n";
   print "�ȉ��̃t�@�C�����A�b�v���[�h���܂���\n";
   print "<table>\n";
   print "<tr><th><tt>�t�@�C����</tt></th><td width=50></td><th><tt>�T�C�Y</tt></th></tr>\n";

   if (! -e $in{'dir'}) {
      @newdir = split(/\//,$in{'dir'});
      foreach (@newdir) {
         if (! -e "$newdir$_") { mkdir("$newdir$_",0755); }
         $newdir .= "$_/";
      }
   }

   while (($key,$val) = each %file) {
      open (FILE,"> $in{'dir'}/$key");
      binmode(FILE);
      print FILE $val;
      close(FILE);
      $size = length($val);
      $k_size = sprintf("%.2f",$size / 1000);
      print "<tr><td><tt><a href='$in{'dir'}/$key' target=_blank>$in{'dir'}/$key</a></tt></td><td width=50></td><td><tt>$k_size KB ($size bytes)</tt></td></tr>\n";
   }

   print "</table>\n";
   print "</form>\n</body>\n</html>\n";

   exit;
}

sub delete {

   if (! ($ref =~ /$script/)) { print "Location:$script\n\n"; }
   if ($in{'f_name2'}) { $in{'f_name'} = $in{'f_name2'}; }
   if (! $in{'f_name'}) { &print_message("�t�@�C���������L���ł�"); }
   if (-e $in{'f_name'}) { unlink($in{'f_name'}); }
   else { &print_message("�w�肳�ꂽ�t�@�C�������݂��܂���"); }

   print "Content-type:text/html; charset=Shift_JIS\n";
   print "Pragma:no-cache\n";
   print "Cache-Control:no-cache\n";
   print "Expires:Thu, 01 Dec 1994 16:00:00 GMT\n\n";
   print "<html>\n<head>\n<title>WEB EDITOR</title>\n$style2";
   print "<script>parent.menu.location.reload(true)</script>\n";
   print "</head>\n<body>\n";
   print "<h2>WEB EDITOR</h2>\n";
   print "<form action='$script' method=post enctype='multipart/form-data'>\n";
   print "<input type=submit name=in value='�t�@�C���̕ҏW'>&nbsp;";
   print "<input type=submit name=uploader value='�t�@�C���A�b�v���[�_'><hr>\n";
   print "$in{'f_name'} ���폜���܂���\n";
   print "</form>\n</body>\n</html>\n";

   exit;
}

sub deldir {

   if (! ($ref =~ /$script/)) { print "Location:$script\n\n"; }
   if (! $in{'dir'}) { &print_message("�f�B���N�g���������L���ł�"); }
   if (! (-e $in{'dir'})) { &print_message("�w�肳�ꂽ�f�B���N�g���͑��݂��܂���"); }
   if ($ENV{'SCRIPT_NAME'} =~ /$in{'dir'}/) { &print_message("Web editor���ݒu���Ă���f�B���N�g���͍폜�ł��܂���"); }

   $st_dir = $in{'dir'};
   &open_dir($in{'dir'});

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

   foreach (reverse sort @lists) {
      $f_type = (stat($_))[2];
      $f_type = substr((sprintf ("%03o",$f_type)),0,2);
      if ($f_type == 40) { rmdir($_); }
      else { unlink($_); }
   }
   rmdir($in{'dir'});

   print "Content-type:text/html; charset=Shift_JIS\n";
   print "Pragma:no-cache\n";
   print "Cache-Control:no-cache\n";
   print "Expires:Thu, 01 Dec 1994 16:00:00 GMT\n\n";
   print "<html>\n<head>\n<title>WEB EDITOR</title>\n$style2";
   print "<script>parent.menu.location.reload(true)</script>\n";
   print "</head>\n<body>\n";
   print "<h2>WEB EDITOR</h2>\n";
   print "<form action='$script' method=post enctype='multipart/form-data'>\n";
   print "<input type=submit name=in value='�t�@�C���̕ҏW'>&nbsp;";
   print "<input type=submit name=uploader value='�t�@�C���A�b�v���[�_'><hr>\n";
   print "$in{'dir'} ���폜���܂���\n";
   print "</form>\n</body>\n</html>\n";

   exit;
}

sub gate {

   print "Content-type:text/html; charset=Shift_JIS\n";
   print "Pragma:no-cache\n";
   print "Cache-Control:no-cache\n";
   print "Expires:Thu, 01 Dec 1994 16:00:00 GMT\n\n";
   print "<html>\n<head>\n<title>WEB EDITOR</title>\n$style2";
   print "</head>\n<body>\n";
   print "<h2>WEB EDITOR</h2>\n";
   print "<form action='$script' method=post enctype='multipart/form-data'>\n";
   print "�p�X���[�h����͂��ă��O�C�����ĉ�����<p>\n";
   print "�p�X���[�h�F<input type=password name=pass>&nbsp;\n";
   print "<input type=submit value='���O�C��'>\n";
   print "</form>\n</body>\n</html>\n";

   exit;
}

sub make_frame {

   print "Content-type:text/html; charset=Shift_JIS\n\n";
   &copy;
   print "<html>\n<head>\n<title>WEB EDITOR</title>\n</head>\n";
   print "<frameset cols=\"$frame_cols,*\">\n";
   print "<frame src=\"$script?menu\" name=\"menu\" scrolling=auto>\n";
   print "<frame src=\"$script?in\" name=\"disp\">\n";
   print "</frameset>\n";
   print "</html>\n";

   exit;
}

sub print_message {

   print "Content-type:text/html; charset=Shift_JIS\n\n";
   print "<html>\n<head>\n<title>WEB EDITOR</title>\n$style2</head>\n<body>\n";
   print "<h2>WEB EDITOR</h2>\n";
   print "$_[0]\n<p>";
   print "<a href='javascript:history.back()'>�߂�</a>";
   print "</body></html>\n";

   exit;
}

sub copy {  # ����\�� �폜�֎~

   print "<!----------------------------------------------------\n";
   print "�� WEB EDITOR $ver (Free Soft)                      ��\n";
   print "�� Copyright (C) 2002 suepon , All rights reserved. ��\n";
   print "�� Script found at http://CGIScriptMarket.com/      ��\n";
   print "----------------------------------------------------->\n";
}
