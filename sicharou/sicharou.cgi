#!/usr/local/bin/perl

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++�@�@[ �������A������N!! ]
#+++		�����>>> All Created by Tacky
#+++		�����>>> Copyright (c) 1999.6 Tacky's Room. All rights reserved....
#+++        Homepage >>> http://tackysroom.com/
#+++
#+++ �ݒu���@�\��(��̗�)
#+++
#+++ public_html�i�z�[���y�[�W�f�B���N�g���j
#+++ |
#+++ |-- cgi-bin�i�C�ӂ̃f�B���N�g���j
#+++   |
#+++   |-- jcode.pl      (755)�c(���{�ꃉ�C�u����)
#+++   |-- sicharou.cgi  (755)�c(�X�N���v�g�{��)
#+++   |-- sicharou.txt  (666)�c(���O�t�@�C��)�c��̂܂܃A�b�v���[�h
#+++   |-- sicharou2.txt (666)�c(���e�񐔊Ǘ��t�@�C��)�c��̂܂܃A�b�v���[�h
#+++   |-- sicharou3.txt (666)�c(��A�l�p���b�Z�[�W�i�[�t�@�C��)�c��̂܂܃A�b�v���[�h
#+++
#+++ �@�@��( )���̓p�[�~�b�b�V�����̒l�ł��B
#+++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

require './jcode.pl';										#���{��R�[�h�ϊ�

$script 			= "./sicharou.cgi";						#<<<���̃X�N���v�g�̖��O
$method 			= "POST";								#<<<METHOD�̎w��iPOST�œ��삵�Ȃ�������AGET)
$logfile 			= "./sicharou.txt";						#<<<���b�Z�[�W�̃��O�t�@�C����
$logfile2 			= "./sicharou2.txt";					#<<<���b�Z�[�W��o�^���Ă��ꂽ���̓o�^�񐔗݌v��ێ�����t�@�C���@�����i���g��Ȃ��ꍇ��''
$logfile3 			= './sicharou3.txt';					#<<<���b�Z�[�W��o�^���Ă��ꂽ���X�ւ̐l�ʃ��b�Z�[�W��o�^����t�@�C��
$lockfile			= './sicharou.lock';					#<<<���b�N�t�@�C���̖��O���w��

$title  			= "�w���A�E������N�x";					#<<<�^�C�g�����w��
$titlelogo 			= "./sicharou.gif";		#<<<��i���Ƀ^�C�g�����S���w�肷��ꍇ�A�t���p�X�Ŏw��B�w�肵�Ȃ��ꍇ�́u""�v
$bgcolor			= "#ffffff";							#<<<�w�i�F
$backpicture 		= "../s-1-yellow.gif";			#<<<�w�i�ɉ摜��\������ꍇ�A�t���p�X�Ŏw��B

$tbgcolor			= '#ffcc00' ;							#<<<���̓t�H�[���̔w�i�F
$submit 			= "���͂���΁`��" ;					#<<<���̓t�H�[���́u���M�v�{�^���ɕ\������镶��

#============================================================================================================================================
#(iMODE�̏ꍇ)
$i_name_sz			= 16 ;									#<<<���O���̕�����
$i_email_sz			= 16 ;									#<<<Email���̕�����
$i_hp_sz			= 16 ;									#<<<Homepage���̕�����
$i_message_sz1		= 16 ;									#<<<���b�Z�[�W���̕�����
$i_message_sz2		= 3 ;									#<<<���b�Z�[�W���̍s�����P�s�e�L�X�g�̏ꍇ�͑ΏۊO
$title_i			= '*���A������N!!!*';						#�^�C�g�����w��
$titlelogo_i		= '';									#�^�C�g���摜���w��
$titlelogo_w		= 95 ;									#<<<�^�C�g���摜�̉���(pixel)
$titlelogo_h		= 16 ;									#<<<�^�C�g���摜�̏c��(pixel)
$i_bgcolor			= '#ffff66' ;							#<<<���e���e��\������ꍇ�̔w�i�F
$i_txcolor			= '#000000' ;							#<<<���e���e��\������ꍇ�̕����F
$i_disp				= 1 ;									#<<<�����\�����Ƀ��X�L�����ȈՕ\���Ƃ���H(0:no 1:yes)
$pagemax_i			= 3 ;									#imode���A�P�y�[�W���ɕ\�����錏��(�e�L���̌���)
$textflg_i			= 2 ;									#<<<���b�Z�[�W���̌`��B�i1:�P�s�e�L�X�g�@2:�����s�e�L�X�g�j
$emailflg_i			= 1 ;									#<<<���[���A�h���X����͂���H(0:���Ȃ� 1:����)
$hpflg_i			= 1 ;									#<<<�t�q�k����͂���H(0:���Ȃ� 1:����)

#(Web�̏ꍇ)
$w_name_sz			= 20 ;									#<<<���O���̕�����
$w_email_sz			= 20 ;									#<<<Email���̕�����
$w_hp_sz			= 20 ;									#<<<Homepage���̕�����
$w_message_sz1		= 40 ;									#<<<���b�Z�[�W���̕�����
$w_message_sz2		= 5 ;									#<<<���b�Z�[�W���̍s�����P�s�e�L�X�g�̏ꍇ�͑ΏۊO
$cellheadbgcolor	= "#99CC00";							#<<<���b�Z�[�W�\�������̃Z���w�i�F
$cellbgcolor1 		= "#ffffcc";							#<<<���b�Z�[�W�\�������̃Z���w�i�F�P
$cellbgcolor2 		= "#ffcc33";							#<<<���b�Z�[�W�\�������̃Z���w�i�F�Q�i�P�ƂQ�ŌJ��Ԃ��\�������j
$pagemax 			= 30 ;									#<<<�P�y�[�W���ɕ\�����錏��
$tsz				= '90%';								#<<<���O�\�����̃e�[�u�����T�C�Y
$textflg			= 2 ;									#<<<���b�Z�[�W���̌`��B�i1:�P�s�e�L�X�g�@2:�����s�e�L�X�g�j
$emailflg			= 1 ;									#<<<���[���A�h���X����͂���H(0:���Ȃ� 1:����)
$hpflg				= 1 ;									#<<<�t�q�k����͂���H(0:���Ȃ� 1:����)

#============================================================================================================================================
$textcolor    		= "#990000";							#<<<���b�Z�[�W�\�������̃e�L�X�g�����F
$linkcolor		    = "#cc6600";							# �����N�F�i���ǃ����N�j
$vlinkcolor			= "#666666";							# �����N�F�i���ǃ����N�j
$alinkcolor	 		= "#ff3300";							# �����N�F�i���������j
$pt					= '10pt';								#�S�̂̃t�H���g�T�C�Y�ipt�w��ȊO��������̂��A�l�m��Ȃ��B(^^�U�j

$url 				= "http://tackysroom.com";				#<<<�߂���URL
$password 			= "pass";								#<<<�Ǘ��҃����e�i���X�p�p�X���[�h�i���O�ҏW�p�j�j
$kanriname			= "abcde";								#<<<�Ǘ��҂̖��O�i�����Ɏw�肳�ꂽ���O�́A�����L���O�ΏۊO�ƂȂ�܂��j
$datamax 			= 300 ;									#<<<�ő�f�[�^�ۑ�����
$messagemax 		= 50 ;									#<<<���K�җp���b�Z�[�W�̍ő匏��
$manual 			= 0 ;									#<<<�Ǘ��l�����ү���ނ�\������H(0:no 1:����̫�т̉��ɕ\�� 2:��ʉ����ɕ\��)

#���A�C�R���̎w��B$icon_gif[3]...[10]�̂悤�ɓK���ɑ��₵�ĉ������ˁB	��imode�ł̓A�C�R���͕\���o���܂���
$icon_flg			= 'yes';								#���e���ɃA�C�R�����g�p���邩�H
#���Ǘ��җp�A�C�R���ƃp�X���[�h���w��B�Ǘ��l�͂P�����A�C�R���o�^�o���܂���B
#  $oiconpass�Ɏw�肵���p�X���[�h�œ��e�����ꍇ�A$oicon_gif�̃A�C�R�����\�������悤�ɂȂ��Ă܂��B
#���̉��́A�摜�T�C�Y�B_w�͕��B_h�͍����ł��B�킩��Ȃ��ꍇ��_w�̕�����0�ɂ��Ă����ĂˁB
#�Ǘ��҃A�C�R���͓��ɕK�v�����ꍇ�́A$oiconpass = '';�Ƃ��ĉ������B
$oicon_gif	  = './d_ahiru.gif' ;		$oiconnm  = 'password';
$oicon_gif_w = 32 ; $oicon_gif_h = 32 ;

#����A�җp�A�C�R���Ɠ��e���̖��O���w��B$jicon_gif[2]...[5]�̂悤�ɓK���ɑ��₵�ĉ������ˁB
#  $jiconnm�Ɏw�肵�����O�œ��e�����ꍇ�A$jicon_gif�̃A�C�R�����\�������悤�ɂȂ��Ă܂��B
#���̉��́A�摜�T�C�Y�B_w�͕��B_h�͍����ł��B�킩��Ȃ��ꍇ��_w�̕�����0�ɂ��Ă����ĂˁB
$jicon_gif[0] = './kuma.gif' ;		$jiconnm[0] = '�`����' ;
$jicon_gif_w[0] = 38 ; $jicon_gif_h[0] = 38 ;
$jicon_gif[1] = './parappa.gif' ;	$jiconnm[1] = '�a����';
$jicon_gif_w[1] = 37 ; $jicon_gif_h[1] = 35 ;

$icon_imode			= 7	;	#imode����̃A�N�Z�X�̏ꍇ�A�Œ�łP�������L�̃A�C�R���̔ԍ���I�����Ă��������B

#�K��җp�A�C�R���ƃA�C�R���̖��O�̎w��B$icon_gif[3]...[10]�̂悤�ɓK���ɑ��₵�ĉ������ˁB
#���̉��́A�摜�T�C�Y�B_w�͕��B_h�͍����ł��B�킩��Ȃ��ꍇ��_w�̕�����0�ɂ��Ă����ĂˁB
$icon_gif[0] = './ball.gif' ;		$iconnm[0] = '�{�[��' ;
$icon_gif_w[0] = 32 ; $icon_gif_h[0] = 32 ;
$icon_gif[1] = './corgi.gif' ;		$iconnm[1] = '�R�[�M�[' ;
$icon_gif_w[1] = 32 ; $icon_gif_h[1] = 32 ;
$icon_gif[2] = './cow.gif' ;		$iconnm[2] = '����' ;
$icon_gif_w[2] = 32 ; $icon_gif_h[2] = 32 ;
$icon_gif[3] = './denchi.gif' ;	$iconnm[3] = '�d�r' ;
$icon_gif_w[3] = 32 ; $icon_gif_h[3] = 32 ;
$icon_gif[4] = './dorayaki.gif' ;	$iconnm[4] = '�h���Ă�' ;
$icon_gif_w[4] = 32 ; $icon_gif_h[4] = 32 ;
$icon_gif[5] = './duck.gif' ;		$iconnm[5] = '���Ђ�' ;
$icon_gif_w[5] = 32 ; $icon_gif_h[5] = 32 ;
$icon_gif[6] = './h_bambi.gif' ;	$iconnm[6] = '�o���r' ;
$icon_gif_w[6] = 32 ; $icon_gif_h[6] = 32 ;
$icon_gif[7] = './h_bear.gif' ;	$iconnm[7] = '����' ;
$icon_gif_w[7] = 32 ; $icon_gif_h[7] = 32 ;
$icon_gif[8] = './h_kaeru.gif' ;	$iconnm[8] = '������' ;
$icon_gif_w[8] = 32 ; $icon_gif_h[8] = 32 ;
$icon_gif[9] = './h_momo.gif' ;	$iconnm[9] = '����' ;
$icon_gif_w[9] = 32 ; $icon_gif_h[9] = 32 ;
$icon_gif[10] = './h_saru.gif' ;	$iconnm[10] = '����P��' ;
$icon_gif_w[10] = 32 ; $icon_gif_h[10] = 32 ;
$icon_gif[11] = './h_usagi.gif' ;	$iconnm[11] = '�����P��' ;
$icon_gif_w[11] = 32 ; $icon_gif_h[11] = 32 ;
$icon_gif[12] = './kappa.gif' ;	$iconnm[12] = '������' ;
$icon_gif_w[12] = 32 ; $icon_gif_h[12] = 32 ;
$icon_gif[13] = './mail.gif' ;		$iconnm[13] = '���[��' ;
$icon_gif_w[13] = 32 ; $icon_gif_h[13] = 32 ;
$icon_gif[14] = './monkey1.gif' ;	$iconnm[14] = '����Q��' ;
$icon_gif_w[14] = 32 ; $icon_gif_h[14] = 32 ;
$icon_gif[15] = './nachan.gif' ;	$iconnm[15] = '�Ȃ������' ;
$icon_gif_w[15] = 32 ; $icon_gif_h[15] = 32 ;
$icon_gif[16] = './oyaji.gif' ;	$iconnm[16] = '�I���W' ;
$icon_gif_w[16] = 32 ; $icon_gif_h[16] = 32 ;
$icon_gif[17] = './panda.gif' ;	$iconnm[17] = '�p���_' ;
$icon_gif_w[17] = 32 ; $icon_gif_h[17] = 32 ;
$icon_gif[18] = './poch.gif' ;		$iconnm[18] = '�|�`' ;
$icon_gif_w[18] = 32 ; $icon_gif_h[18] = 32 ;
$icon_gif[19] = './risu.gif' ;		$iconnm[19] = '�肷' ;
$icon_gif_w[19] = 32 ; $icon_gif_h[19] = 32 ;
$icon_gif[20] = './ebi.gif' ;		$iconnm[20] = '�C�V' ;
$icon_gif_w[20] = 32 ; $icon_gif_h[20] = 32 ;
$icon_gif[21] = './tamago.gif' ;	$iconnm[21] = '�ʎq' ;
$icon_gif_w[21] = 32 ; $icon_gif_h[21] = 32 ;
$icon_gif[22] = './takoyaki.gif' ;	$iconnm[22] = '�����Ă�' ;
$icon_gif_w[22] = 32 ; $icon_gif_h[22] = 32 ;
$icon_gif[23] = './tulip.gif' ;	$iconnm[23] = '�`���[���b�v' ;
$icon_gif_w[23] = 32 ; $icon_gif_h[23] = 32 ;
$icon_gif[24] = './usa2.gif' ;		$iconnm[24] = '�����Q��' ;
$icon_gif_w[24] = 32 ; $icon_gif_h[24] = 32 ;
$icon_gif[25] = './volley.gif' ;	$iconnm[25] = '�o���[�{�[��' ;
$icon_gif_w[25] = 32 ; $icon_gif_h[25] = 32 ;

#�A�C�R���ꗗ��\������ہA�P�s�ɃA�C�R�������\�����܂��H
$icon_line					= 5 ;	#���̏ꍇ�A�T�\����������s������Ď��ł��B

#<<<Web����̃A�N�Z�X���A��ʉ����ɕ\������Ǘ��҂���̃��b�Z�[�W�B"EOM"�`EOM�̍s�܂łɕK������Ă��������B���b�Z�[�W�s�v�̏ꍇ�́A$manualmsg�̍s����EOM�̍s�܂őS�č폜���Ă�
$manualmsg = <<"EOM";
<table border=0 width=50%  cellspacing=0 cellpadding=5><tr><td bgcolor=#ffffcc>
���͂���΁[�I�l�u������N�v�͉�����\�\\���܂��ƁA�R�~���j�P�[�V������
�Ƃ�ׂɂƂ��Ă���؂Ȏ��A����!!�w���A�x�ł�!!....���A���܂���`�I�������ꂾ���B�i�΁j
<br>�l�̎g�����́u���O�������āA�|����@�����������`��v�Ł`��</font>
<br><font size=2 color=#333333> ���⑫�F�w���͂���΁`��x�́A�݂Ȃ��񂪂����A���Ă���邩
�킩��Ȃ�����A�u���͂悤�v�A�u����ɂ��́v�A�u����΂��v���~�b�N�X���Ă݂܂����`��i�΁j</font>
<br><b><font size=+1>iMode�ł������܂�</font></b>
</td></tr></table>
EOM

#<<<imode����̃A�N�Z�X���A��ʉ����ɕ\������Ǘ��҂���̃��b�Z�[�W�B"EOM"�`EOM�̍s�܂łɕK������Ă��������B���b�Z�[�W�s�v�̏ꍇ�́A$manualmsg2�̍s����EOM�̍s�܂őS�č폜���Ă�
$manualmsg2 = <<"EOM";
�݂�ȋC�y�ɏ������݂��Ăˁ`��
EOM

#���������Z�L�����e�B������
$postchk		= 1;		#���e���E�����e�i���X����Method��POST����ɂ���ꍇ�͂P�B�ȊO�͂O�B
$urlchk			= '';	#�����Ŏw�肳�ꂽ�A�h���X(CGI�̐ݒu�A�h���X���L��)�ȊO���瓊�e���������ꍇ���G���[�Ƃ��܂��B�ݒ肵�Ȃ��ꍇ��''

$urllink		= 2 ;		#�^�C�g���y�і{����http����̃����N����������G���[�ɂ���H
							#(0:���Ȃ� 1:URL�͑S�Ă��� 2:�ȉ���$urlerr�Ŏw�肳�ꂽ�������܂܂�Ă���URL�̂݃G���[�Ƃ���
#��$urllink=2�̏ꍇ�A�ȉ��Ɏw�肵���������܂�URL���G���[�Ƃ���
$urlerrnm[0]	= 'exe';
$urlerrnm[1]	= 'virus';
$kaigyo			= 0;		#�w��l���̉��s���A�������ꍇ�A�P�s���s�ɒu�����܂��B�@���w�肵�Ȃ��ꍇ��0
$name_comment	= 'coxmment';#����I�ɓ��e���Ă���悤�Ȏ����������炱�̖��O��K���ɕς��Ă݂ĉ������B�������e�X�N���v�g�̎�ނɂ���Ă͑S�R�Ӗ��������ǁB
@errword 		= ('','');	#���e�֎~���@ex.@errword = ('����','�e�X�g�e�X�g');
$urlcnt			= 2;		#���b�Z�[�W���ɋL���o����URL�̌��@���w�肵�Ȃ��ꍇ��0
$japan			= 1;		#���b�Z�[�W����"�S�p����/���p�J�i(�A�����p�J�i�͕����������鎖������܂�)"���P�����ł�������΃G���[�Ƃ���H(0:no 1:yes)
$mailerr		= 0;		#���A�h������͂��ꂽ��G���[�ɂ���H(0:no 1:yes)�@�����������c�[���̓��A�h���w�肵�Ă��鎖�������ׂ����ăG���[�Ƃ��Ă݂�
$urlerr			= 0;		#URL������͂��ꂽ��G���[�ɂ���H(0:no 1:yes)�@�����������c�[����URL���w�肵�Ă��鎖�������ׂ����ăG���[�Ƃ��Ă݂�
#���������Z�L�����e�B������

#�X�N���[���o�[�̐F�ύX�B�悭�킩��Ȃ����́A"EOM"�̎��̍s����擪��EOM�̍s�̊Ԃ��폜���ĂˁB
$scrollbar = <<"EOM";
BODY{
scrollbar-base-color : #eeeeee;
}
EOM

$tag				= 'no';									#�^�O����(yes,no)
@errtag = ('table','meta','form','!--','embed','html','body','tr','td','th','a');		#�f���W�����`�ȃ^�O

#=============================================================================================================================================================================================
#�t�H�[���b�r�r�ݒ�@("EOM"�`EOM�̊ԂɃ��b�Z�[�W�������Ă��������j
#���g�p���Ȃ��ꍇ�́A$css_style = "";�Ƃ��A��������Q�s(�擪��EOM�̍s�܂ł�)���폜���ĉ������B
$css_style = <<"EOM";
STYLE=font-size:$pt;color:#0f642d;background-color:#ffffcc;border-style:solid;border-color:#4d9900;border-width:1;
EOM

#���g���ۂ�����ꍇ�A�����ݒ�ł͔w�i�F�𔒈ȊO�ɂ�����Y��ɕ\������Ȃ��ł��B���F�ɍ��������߉摜�����K�v������܂��B�����́u�������ݑ��v�̐����y�[�W���݂ĂˁB
$maru						= 0 ;	#���̓t�H�[���̎l�p�g���ۂ����܂����H (0:no 1:yes) ��Web�̂�
$top_l						= './top_l_h.gif';			#���b�Z�[�W��������̓��߉摜���w�聦�l�p�g���ۂ����Ȃ��ꍇ�͑ΏۊO
$top_r						= './top_r_h.gif';			#���b�Z�[�W���E����̓��߉摜���w�聦�l�p�g���ۂ����Ȃ��ꍇ�͑ΏۊO
$bottom_l					= './bottom_l_h.gif';		#���b�Z�[�W���������̓��߉摜���w�聦�l�p�g���ۂ����Ȃ��ꍇ�͑ΏۊO
$bottom_r					= './bottom_r_h.gif';		#���b�Z�[�W���E�����̓��߉摜���w�聦�l�p�g���ۂ����Ȃ��ꍇ�͑ΏۊO

$rankcnt					= 20 ;	#�����L���O��ʉ��l�������L���O�ꗗ��ʂɕ\�����܂����H

#���j���J�E���g�ݒ�B�w�肵�����e�񐔂ɒB����ƁA���j�����b�Z�[�W��\�����܂��B�s�v�̏ꍇ�́A@OIWAI�̍s���폜���ĂˁB
@OIWAI = (0,2,10,30,50,80,120,170,230,300,400,600,1000,1500,2500,4000);
$oiwaibgcolor = "#CC0000";	#���j���J�E���g�̏ꍇ�̔w�i�F
$oiwaitxcolor = "#ffffff";	#���j���J�E���g�̏ꍇ�̕����F
#���j�����b�Z�[�W�\���̍ۂ̕��́BNAME��CNT�̕����ɂ͂��̐l�̖��O�ƒB���񐔂��u������܂��̂ŁA
#�K��NAME�ECNT�Ƃ��������͓���Ă����Ă��������B
$oiwaimsg = "<font size=+1>NAME����!!   ���e�񐔂�CNT��ɒB�������i���܂���!!!!!</font>";

$oiwaitxcolor_i = "#000000";	#���j�����b�Z�[�W�̕����F�i�g�сj
$oiwaimsg_i = "NAME���񓊍e�񐔂�CNT��ŏ��i���܂���!";	#���j�����b�Z�[�W(�g��)

#�f���r�炵�΍�B�r���������v���o�̃A�h���X��ݒ肵�ĉ������B
#�@"xxx?.com"�Ƃ����ꍇ�A"xxx1.com","xxx2.com"���A�u�H�v�̕�����������P�Ɣ��f���܂�
#  "xxx*.com"�Ƃ����ꍇ�A"xxx1.com","xxx12345.com���A�u���v�̕������O�ȏ�̕�����Ɣ��f���܂��B
#��F@DANGER_LIST=("xxx.com","yyy.com","zzz*.or.jp");
@DANGER_LIST=("","","");

#�f���r�炵�΍􂻂̂Q�B���b�Z�[�W�ő啶�������w��B���ɐݒ肵�Ȃ��ꍇ�́A''�Ƃ��ĉ������B
$maxword = '1000' ;

$renchan1		= 0 ;		#�w�蕪�ȓ��̘A�����e�ʹװ�Ƃ���B�ݒ肵�Ȃ��ꍇ��0�Ƃ��ĂˁB
$renchan2		= 0 ;		#�w��񐔈ȏ�̘A�����e�ʹװ�Ƃ���B�ݒ肵�Ȃ��ꍇ��0�Ƃ��ĂˁB

$method 			= "POST";								#<<<METHOD�̎w��iPOST�œ��삵�Ȃ�������AGET)

#����L�ɂ���u@OIWAI�v�Ɏw�肵���񐔂ŏ��i���Ă����܂��B@OIWAI�Ɠ��������ݒ肵�ĉ������B
@rank	= ('�c�t����','���w�Z��w�N','���w�Z���w�N','���w�Z���w�N','���w��','���Z��','��w��','���Ј�','�W��','�ے�','����','�햱','�ꖱ','�В�','�');
#�����i�ɉ摜���g���ꍇ�A���i�񐔂Ɠ��������ݒ肵�Ă��������B��$rankicon[n]�͕K���u0�v����n�܂�܂��B�摜���g��Ȃ�������''�Ƃ��ĂˁB
#�@�摜�̕��E�������킩��Ȃ��l�́A$rankicon_w[n] = 0 ; $rankicon_h[n] = 0 ;�̂悤�Ɂu0�v�Ƃ��ĉ������B
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

$damedame		= 0 ;	#Location�w�b�_���g���Ȃ��T�[�o�[��1�B�ʏ��0�ł����͂��B���g�N�g�N�A3nopage,WinNT�T�[�o�[����1���ȁB

$frame_home			= '';			#[HOME]�������̃^�[�Q�b�g�w��B�t���[���y�[�W���g���Ă��Ȃ��l�͂��̂܂܂ł����ł��B
$frame_other		= '';			#[���i���][�ꊇ���X]���̉������̃^�[�Q�b�g�w��B�t���[���y�[�W���g���Ă��Ȃ��l�͂��̂܂܂ł����ł��B

$passsw			= 1;		#���̓t�H�[���Ƀp�X���[�h����t����H(0:no 1:yes)�@�t�����瓊�e�҂������̋L�����C���A�폜�o���܂���
$host_disp		= 0;		#�����[�g�z�X�g��\������H(0:no 1:yes)
#���e���̃p�X���[�h��crypt�֐����g�p����i�Í����j
#crypt�֐������p�o���Ȃ��ꍇ������܂��̂ŁA���e���ɃG���[�ɂȂ�ꍇ�́A�u0:�g�p���Ȃ��v�ɂ��ĉ������ˁB
$ango			= 1 ;	#0:�g�p���Ȃ� 1:�g�p����@�i�����F�P�F�g�p����j

$dsp_new		= 1;		#�g�ѱ������A�u�V�K���e̫�сv��ʉ�ʂŕ\������H(0:no 1:yes)

#<<<�@�������牺�͂�����Ȃ������g�̂��߂ł��B(^_^;
utime time(), time(), __FILE__; 								# �X�N���v�g���������̍X�V

#������Web����̃A�N�Z�X���炩�g�т���̃A�N�Z�X���𔻒f
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

###<--- �V�X�e�������E�����擾 ------------------------------------
$ENV{'TZ'} = "JST-9";
$iday = time - ( $renchan1 * 60 ) ;  #$renchan1���O
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
#<<<COOKIE�̎擾
&cookieget;
#<<<�t�H�[���f�R�[�h���ϐ����
&decode ;
if ( $FORM{'action'} eq "maintenance" ) {      			#<<<"����"�������e�i���X�̏ꍇ
	&Maintenance;
}	elsif	( $FORM{'action'} eq "update" )		{		#<<<���O�t�@�C���X�V
	&update ;
}	elsif	( $FORM{'action'} eq "update2" )	{		#<<<���K�җp���b�Z�[�W�t�@�C���X�V
	&update2 ;
}	elsif	( $FORM{'action'} eq "ranking" )	{		#<<<�����L���O�\��
	&ranking ;
}	elsif	( $FORM{'action'} eq "download" )	{		#<<<�_�E�����[�h
	&download ;
}	elsif   ( $FORM{'action'} eq "icondisp" )	{		#<<<�A�C�R���ꗗ�\��
	&icondisp ;
}	elsif   ( $FORM{'action'} eq "info" )	{			#<<<���i���i����
	&info ;
}	elsif   ( $FORM{'action'} eq "input" )	{			#<<<���̓t�H�[���̕\��
	&header ;
	&header2 ;
	&inputform ;
	&footer ;						   			#<<< html�t�b�^�[�̏o��
}	else	{
	if ( $FORM{'action'} eq "regist" ) {	   			#<<<"����"���o�^�̏ꍇ
	 	&regist; 								#���O�o�^����
		if ( $acs == 0 )	{
			if ( $damedame == 0 )	{
				print "Location: $script?\n\n";
			}	else	{
				print "Content-type: text/html\n\n";
				print "<html><head><META HTTP-EQUIV=\"Refresh\" CONTENT=\"0; URL=";
				print "$script?\">";
				print $dmy_tok2_cookie; # �N�b�L�[�̔���
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
	&disp ;							   			#<<<�o�^�σ��b�Z�[�W�̕\��
	if ( $manual == 2 )	{	&setumei;	}	#<<<�u�g�����v�̕\��
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
	print "<option value=\"edit\">�ҏW";
	print "<option value=\"delete\">�폜";
	print "<option value=\"message\">�K��҃��b�Z�[�W";
	print "</select>\n";
	if ( $acs == 1 ) { print "<br>\n";	}
	print "<input type=hidden name=\"action\" value=\"maintenance\">\n";
	print "<input type=submit value=\"ADMIN\" $css_style>\n";
	#<<<�@�������Ȃ��Ńl��
	print "<br>\n";
	if ( $env == 0 ) {
		print "<a href=http://tackysroom.com target=_top>sicharou(Ver0.996)-Tacky\'s Room</a>\n";
	}	else	{
		print "<!-- sicharou Ver0.996 Created by Tacky\'s Room (URL:http://tackysroom.com) -->\n";
	}
	print "</form>";
	print "</div>\n" if ( $acs == 0 );
	&footer ;						   			#<<< html�t�b�^�[�̏o��
}
###############################################################################
#### Main Process  END  #######################################################
###############################################################################

###<--------------------------------------------------------------
###<---   �f�R�[�h���ϐ����
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
	        #�댯�ȃ^�O�͋֎~!!!
			foreach ( @errtag )	{
				if ($value =~ /<$_(.|\n)*>/i) {&error("�g�p�o���Ȃ��^�O�����͂���Ă��܂�");}
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
				#�S�p/���p�J�i�܂܂Ȃ��H
				if ($chk !~ /[\xA1-\xFE][\xA1-\xFE]/) {		$dat =~ tr/a-z/A-Z/;}
				&jcode'convert(*chkvalue, "euc");
				if ($chkvalue !~ /[\xA1-\xFE][\xA1-\xFE]/) {	$chkvalue2 =~ tr/a-z/A-Z/;	}
				#����������
				if ( index($chkvalue2,$dat) >= 0 ) {
					&error("���e�֎~�P�ꂪ���͂���Ă��܂��̂œ��e�o���܂���");
				}
			}
		}
		if ( $urllink && ($name eq 'name' || $name eq 'hp' || $name eq 'msg' || $name eq $name_comment )) {
			if ( $urllink == 1 ) {
				if ( $value =~ /tp:\/\//i && $name ne 'hp' ) {
					&error("�Z�L�����e�B�΍�ׁ̈AURL�͓��͏o���܂���B");
				}
			}	else	{
				foreach $buf ( @urlerrnm ) {
					if ( $value =~ /([^=^\"]|^)(http|ftp)([\w|\!\#\&\=\-\%\@\~\;\+\:\.\?\/]+)/i ) {
						if ( $3 =~ /$buf/ ) {
							&error("�����u$buf�v�́A�Z�L�����e�B�΍�ׁ̈A���͏o���܂���B");
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
		if ( $postchk && !$post )	{	&error("�s���ȓ��e�ł��B");	}
		if ( $urlchk && $ENV{HTTP_REFERER} !~ /$urlchk/i )	{	exit;	}
	}
	$FORM{$name_comment} =~ s/\r\n/<br>/g;	$FORM{$name_comment} =~ s/\r|\n/<br>/g;
	$FORM{'hp'}   =~ s/^http\:\/\///;
	if ( $acs == 1 )	{	$FORM{'icon'} = $icon_imode ;	}
}
###<--------------------------------------------------------------
###<---   HTML�w�b�_�[�����o��
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
		print "<meta http-equiv=\"Pragma\" content=\"no-cache\">\n";	#ezweb�Ή�
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
###<---   HTML�t�b�_�[�����o��
###<--------------------------------------------------------------
sub footer {
	print "</body></html>\n";
}
###<--------------------------------------------------------------
###<---   ���O�t�@�C���ǂݍ���
###<--------------------------------------------------------------
sub	dataread	{
	#<<<���O�ǂݍ���
	if ( !(open(IN,"$logfile")))	{	&error("���O�t�@�C��($logfile)�̃I�[�v���Ɏ��s���܂���");	}
	@LOG = <IN>;
	close(IN);
}
###<--------------------------------------------------------------
###<---   �w�b�_�[�Q
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
			print "<td width=5>&nbsp;</td><td><INPUT TYPE=button VALUE=\"�����L���O\" ";
			if ( $frame_other ) {
				print "onClick=\"parent.$frame_other.location.href = \'$script?action=ranking\'\" $css_style></td></form>\n";
			}	else	{
				print "onClick=\"parent.location.href = \'$script?action=ranking\'\" $css_style></td></form>\n";
			}
		}
		if ( $logfile2 && $FORM{'action'} ne 'download')	{
			print "<form>\n";
			print "<td width=5>&nbsp;</td><td width=10%><INPUT TYPE=button VALUE=\"���i���i����\" ";
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
			print "&nbsp;<a href=$script?action=ranking>[�����L���O]</a>";
		}
		print "&nbsp;<a href=$script?action=input>[�V�K���e]</a>" if ( $dsp_new == 1 ) ;
		print "<br><br>\n";
	}
	if ( $titlelogo )	{
		print "<img src=\"$titlelogo\"><br>\n";
	}	else	{
		print "$title<br>\n";
	}
}
###<--------------------------------------------------------------
###<---   ���̓t�H�[��
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
		#�������O
		print "&nbsp;&nbsp;Name</td>";
		print "<td bgcolor=\"$tbgcolor\"><input type=text name=\"name\" size=$name_sz value=\"$c_name\" $css_style></td>\n";
		print "<td bgcolor=\"$tbgcolor\" align=\"center\" rowspan=4>";
		print "<textarea name=\"$name_comment\" cols=$message_sz1 rows=$message_sz2 $css_style>$c_cm</textarea>&nbsp;&nbsp;<br>";
		if ( $passsw == 1 ) {
			print "�p�X���[�h<input type=\"password\" name=\"pass\" size=\"8\" value=\"$c_ps\" $css_style>&nbsp;&nbsp;\n";
		}
		print "<input type=submit value=$submit $css_style>";
		if ( $icon_flg eq 'yes' )	{	print "&nbsp;&nbsp;<a href=\"$script?action=icondisp\">�A�C�R���ꗗ</a>";	}
		print "</td></tr>\n";
		#���A�C�R��
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
			#�����[���A�h���X
			print "<tr><td bgcolor=\"$tbgcolor\">\n";
			print "&nbsp;&nbsp;Email</td><td bgcolor=\"$tbgcolor\"><input type=text name=\"email\" size=$email_sz value=\"$c_email\" $css_style>&nbsp;&nbsp;</td></tr>\n";
		}
		if ( $hpflg == 1 ) {
			#��Homepage
			print "<tr><td bgcolor=\"$tbgcolor\">\n";
			print "&nbsp;&nbsp;URL</td><td bgcolor=\"$tbgcolor\"><input type=text name=\"hp\" size=$hp_sz value=\"http://$c_hp\" $css_style>&nbsp;&nbsp;</td></tr>\n";
		}
		print "</table>\n";
	}	else	{
		print "<input type=text name=\"$name_comment\" size=$message_sz1 value=\"$c_cm\" $css_style>\n";
		print "<input type=submit value=$submit $css_style>";
		if ( $passsw == 1 ) {
			print "&nbsp;&nbsp;�p�X���[�h<input type=\"password\" name=\"pass\" size=\"8\" value=\"$c_ps\" $css_style>&nbsp;&nbsp;\n";
		}
		if ( $emailflg == 1 || $hpflg == 1 )	{
			if ( $icon_flg eq 'yes' )	{
				print "&nbsp;&nbsp;<a href=\"$script?action=icondisp\">�A�C�R���ꗗ</a>&nbsp;&nbsp;\n";
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
				print "&nbsp;&nbsp;<a href=\"$script?action=icondisp\">�A�C�R���ꗗ</a>\n";
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

	}	else	{		#imode��
		#�������O
		print "��Name<br>";
		print "<input type=text name=\"name\" size=$name_sz value=\"$c_name\"><br>\n";
		if ( $emailflg == 1 ) {
			#�����[���A�h���X
			print "��Email<br><input type=text name=\"email\" size=$email_sz value=\"$c_email\"><br>\n";
		}
		if ( $hpflg == 1 ) {
			#��Homepage
			print "��URL<br><input type=text name=\"hp\" size=$hp_sz value=\"http://$c_hp\"><br>\n";
		}
		print "��Message<br>";
		if ( $textflg != 1 )	{
			print "<textarea name=\"$name_comment\" cols=$message_sz1 rows=$message_sz2 $css_style>$c_cm</textarea><br>";
		}	else	{
			print "<input type=text name=\"$name_comment\" size=$message_sz1 value=\"$c_cm\">\n";
		}
		print "<br><input type=submit value=$submit>";
	}
	print "</form>";

	if ( $manual == 1 )	{	&setumei;	}	#<<<�u�g�����v�̕\��

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
###<---   �݂Ȃ��񂩂�̈��A��\��
###<--------------------------------------------------------------
sub	disp	{

	if ( $acs == 0 )	{
		print "<center>\n";
		print "<br><font size=+2>$title</font><br><br>\n" if ( $FORM{'action'} eq 'download' ) ;;
		if ( !(open(IN3,"$logfile3")))	{	&error("���O�t�@�C���R($logfile3)�̃I�[�v���Ɏ��s���܂���");	}
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
			print "<td bgcolor=$cellheadbgcolor nowrap align=center><font color=#000000>��</font></td>";
			print "<td bgcolor=$cellheadbgcolor nowrap width=10% align=center><font color=#000000>���i���</font></td>";
		}
		print "</tr>\n";
	}	else	{
		if ( !(open(IN3,"$logfile3")))	{	&error("���O�t�@�C���R($logfile3)�̃I�[�v���Ɏ��s���܂���");	}
		@message = <IN3>;
		close(IN3);
		foreach ( @message ) {
			($n,$m) = split(/:/,$_);
			if ( $c_name eq $n )	{
				print "��MESSAGE<br><b>$m</b>\n";
			}
		}
	}
	if ( !(open(IN,"$logfile")))	{	&error("���O�t�@�C��($logfile)�̃I�[�v���Ɏ��s���܂���");	}
	@data = <IN>;	close(IN);

	#�\���Ώۃy�[�W�̐擪�f�[�^�������Z�o
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
				if ( $cm eq '' ) {	$cm = '�@';	}
				$cm =~ s/&amp;/&/g;
				print "<td bgcolor=$bg ><font color=$textcolor>$cm";
				print " ...($hst)" if ( $host_disp == 1 ) ;
				print "</font></td>\n";
				if ( $logfile2 )	{	#i001112
					print "<td bgcolor=$bg align=right width=60><font color=$textcolor>$raihoucnt��</font></td>\n";
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
				print "($raihoucnt��c$rank[$ranking])\n";
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
			print "<br>TotalCount�́A���Ȃ��̉ߋ�����̈��A�񐔂ł���</font><br><br>";
		}
	}	else	{
		print "( )�̐����͓��e�񐔂ł�\n";
	}
	if ( $acs == 0 )	{	#i001112
		print "<hr size=1 noshade color=#000000>\n" ;
		print "<form action=\"$script\" method=\"$method\">\n";
		print "<input type=hidden name=\"action\" value=\"download\">\n";
		print "<input type=submit value=\"���O���_�E�����[�h\" $css_style>\n";
		print "<br>�g���q��htm�ɕύX���ĉ�����";
		print "</form>\n";
	}
}
###<--------------------------------------------------------------
###<---   ���A���O�o��
###<--------------------------------------------------------------
sub	regist	{
	if ( $FORM{'name'} eq "")	{	&error("���O�͏ȗ��o���܂���B") ;	}
	if ( $maxword ne '' && (length($FORM{$name_comment}) > $maxword))	{	&error("���b�Z�[�W��$maxword�����܂ł����o�^�o���܂���B");	}
	if ( $textflg2 == 1 && $FORM{$name_comment} eq '' )	{	&error("���b�Z�[�W���͏ȗ��o���܂���B") ;	}
	if ( $mailerr == 1 && $FORM{'email'} ) { &error("�Z�L�����e�B�΍�ׁ̈A���[���A�h���X�͓��͏o���܂���B");	}
	if ( $urlerr == 1 && $FORM{'hp'} ) { &error("�Z�L�����e�B�΍�ׁ̈AURL�͓��͏o���܂���B");	}
	# URL�Ɠ������̂��{���ɂ��������`
	if ($FORM{'hp'}){
		if ( $FORM{$name_comment} =~ /$FORM{'hp'}/) {
			&error("��`���e�ƌ��Ȃ���܂��̂œ��e�o���܂���");
		}
	}
	if ( $urlcnt ) {
		$urlnum = ($FORM{$name_comment} =~ s/(h?ttp)/$1/ig);
		if ( $urlnum > $urlcnt ) { &error("URL��" . ($urlcnt + 1) . "�ȏ�͋L���o���܂���"); }
	}
	if ( $japan ) {
		$str = $FORM{$name_comment};
		jcode::convert(\$str, 'euc','sjis');
		if($str =~ /[\xA1-\xFE][\xA1-\xFE]/ || $str =~ /\x8E/ || $str =~ /[\x8E\xA1-\xFE]/){
		}	else	{
			&error("���p�p�����݂̂̓��e�͏o���܂���B");
		}
	}

	# �z�X�g�����擾
	$host  = $ENV{'REMOTE_HOST'};	$addr  = $ENV{'REMOTE_ADDR'};
	if ($host eq "" || $host eq "$addr") {
		($p1,$p2,$p3,$p4) = split(/\./,$addr);
		$temp = pack("C4",$p1,$p2,$p3,$p4);
		$host = gethostbyaddr("$temp", 2);
		if ($host eq "") { $host = $addr; }
	}
	#�f���r�炵�΍�
	foreach $buf(@DANGER_LIST){
		if ( $buf ) {
			# �p�^�[���}�b�`��ϊ�
			$buf=~ s/\./\\./g;		$buf=~ s/\?/\./g;		$buf=~ s/\*/\.\*/g;
			if($host =~ /$buf/gi){	&error("\�\\��\�󂠂�܂���B<br>���Ȃ��̃v���o�C�_�[����͓��e�ł��܂���ł����D ");	}
		}
	}
	&filelock ;		#�t�@�C�����b�N
	&dataread ;
	$dcnt2 = @LOG;
	if ($dcnt2 >= $datamax) {	pop(@LOG);	}
	if ( $dcnt2 < 1 )	{
		$no = 1;										#�P����
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
				if ( $write_cnt >= $renchan2 )	{	&fileunlock ;	&error("$renchan2��ȏ�̘A�����e�͋֎~���Ă��܂�");	}
			}
			if ( $renchan2 != 0 && $hst ne $host )	{	last ; }	#i001220
			if ( $renchan1 != 0 && $dt ge $renday )	{
				if ( $hst eq $host )	{	&fileunlock ;	&error("$renchan1���ȓ��̘A�����e�͋֎~���Ă��܂�");	}
			}
		}
	}
	if ( $logfile2 )	{
		if ( !(open(IN2,"$logfile2")))	{	&fileunlock ;	&error("���O�t�@�C���Q($logfile2)�̃I�[�v���Ɏ��s���܂���");	}
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
		if ( !(open(OUT,">$logfile2")))	{	&fileunlock ;	&error("���O�t�@�C��($logfile)�̃I�[�v���Ɏ��s���܂���");	}
		print OUT @sv;
		close(OUT);
	}
	# �p�X���[�h�̈Í����icrypt�֐��g�p�j�j
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

	if ( !(open(OUT,">$logfile")))	{	&fileunlock ;	&error("���O�t�@�C��($logfile)�̃I�[�v���Ɏ��s���܂���");	}
	print OUT @LOG;
	close(OUT);
	&fileunlock ;	#�t�@�C�����b�N����

	#COOKIE�ݒ�
	&cookieset ;
}
###<--------------------------------------------------------------
###<---   �g�����̐�������
###<--------------------------------------------------------------
sub setumei	{
	print "<hr size=1 noshade color=#000000><br>\n";
	#�g������\������
	if ( $acs == 0 ) {	print $manualmsg;	}
	else	{ print $manualmsg2;	}
}
###<-------------------------------------------------------------
###<---   �N�b�L�[�擾
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
###<---   �N�b�L�[�ݒ�
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
###<---   �����e�i���X���[�h
###<--------------------------------------------------------------
sub Maintenance {
	if ( $FORM{'proc'} ne 'message' && $FORM{'no'} eq "")	{	&error("�����e�i���X�Ώۂ̋L��No���w�肵�ĉ������B");	}
	if ( $FORM{'pass'} eq "")	{	&error("�p�X���[�h����͂��ĉ������B");	}

	#���e���O�̃����e�i���X
	if ( $FORM{'proc'} eq 'edit' )	{
		&logmtn;
	}
	#���e���O�̍폜
	if ( $FORM{'proc'} eq 'delete' )	{
		&update;
	}
	#�K��җp���b�Z�[�W�̃����e�i���X
	if ( $FORM{'proc'} eq 'message' )	{
		&msgmtn;
	}
}
###<--------------------------------------------------------------
###<---   ���O�t�@�C���E�����e�i���X
###<--------------------------------------------------------------
sub logmtn {
	if ( $FORM{'no'} eq "")		{	&error("�L��No����͂��ĉ������B");	}
	if ( $FORM{'pass'} eq "")	{	&error("�p�X���[�h����͂��ĉ������B");	}

	$found = 0 ;
	&dataread ;																#<<<���O�ǂݍ���
	foreach ( @LOG )	{
		($no,$dt,$nm,$cm,$cnt,$icon,$email,$hp,$hst,$ps) = split(/,/,$_);
		if ( $FORM{'no'} eq $no )	{
			$ps =~ s/\n//;
			if ($FORM{'pass'} ne $password && (&pass_dec($ps))) { &error("�p�X���[�h���Ⴂ�܂��B"); }
			$found = 1 ;
			if ( $FORM{'proc'} eq "delete" )	{
				&update ;
				exit;
			}
			if ( $cm eq 'OIWAI' ) {&error("���i���b�Z�[�W�f�[�^�͏C���o���܂���B"); }
			&header ;
			$c_name = $nm ;	$c_icon = $icon ;	$c_email = $email ;	$c_hp = $hp ;
			$c_ps = $ps; $c_cm = $cm; $c_cm =~ s/<br>/\n/gi;
			$c_ps = $FORM{'pass'};
			&inputform ;
			last;
		}
	}
	if ( $found == 0 )	{
		&error("�Y������L��No�̃f�[�^�͑��݂��Ă��܂���B");
	}
	&footer ;
	exit;

}
###<--------------------------------------------------------------
###<---   ���K�җp���b�Z�[�W�t�@�C���E�����e�i���X
###<--------------------------------------------------------------
sub msgmtn {

	if ( !(open(IN,"$logfile3")))	{	&error("���O�t�@�C���R($logfile3)�̃I�[�v���Ɏ��s���܂���");	}
	@data = <IN>;	close(IN);

	&header ;
	print "<a href=$script>[BACK]</a>\n";
if ( $acs == 0 )	{
	print "<center>\n";
print <<"EOM";
<table cellpadding=7><tr><td bgcolor=#990000><font color=#ffffff>
<pre>
�����K�Җ��ɓ���̃��b�Z�[�W��\\������ݒ���s���܂���

���K�҂��N�b�L�[�������Ă���ꍇ�A�����œo�^�������O�̐l���A�N�Z�X����
�ۂɐݒ肵�����b�Z�[�W���\\������܂�
<hr>
�ݒ���@�́A�u�K��҂̖��O�v+�u:�i���p�R�����j�v�{�u�\\�����b�Z�[�W�v�{�u���s�v��
����l�l�̃��b�Z�[�W�ƂȂ�܂��B
���͂̓r���ŉ��s�����ꍇ�̓��b�Z�[�W��&lt;br&gt;�����Đݒ肵�ĉ������B<br>
�@��F
�@�@�`����:�������Ă���Ă��肪�Ƃ�
�@�@�a����:���΂炭���ĂȂ��˂��E�E�E
�@�@�b����:�b����ցI&lt;br&gt;&lt;b&gt;�a�������߂łƁ[!!!&lt;/b&gt;
�@�@���^�O��}���\\�ł��B
</td></tr></table>
EOM
}	else	{
print <<"EOM";
<br>�����K�Җ��̃��b�Z�[�W�ݒ聡<br>
<hr>
�u�K��҂̖��O�v+�u:�i���p�R�����j�v�{�u�\\�����b�Z�[�W�v�{�u���s�v��
����l�l�̃��b�Z�[�W�ƂȂ�܂��B
���͂̓r���ŉ��s�����ꍇ�̓��b�Z�[�W��&lt;br&gt;�����Đݒ肵�ĉ������B<br>
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
		print "<br><input type=submit value=�K��҃��b�Z�[�W���X�V����>\n";
		print "</form></center>\n";
	}	else	{
		print "<textarea name=\"msg\" cols=$message_sz1 rows=$message_sz2 >$BUF</textarea>\n";
		print "<br><input type=submit value=�X�V>\n";
		print "</form>\n";
	}
	&footer ;
	exit ;
}
###<--------------------------------------------------------------
###<---   ���O�t�@�C���X�V
###<--------------------------------------------------------------
sub update {

	@DELWORD = split(/ /,$FORM{'no'});

	&filelock ;		#�t�@�C�����b�N
	&dataread ;
    foreach (@LOG) {
		($no,$dt,$nm,$cm,$cnt,$icon,$email,$hp,$hst,$ps) = split(/,/,$_);
        if ($FORM{'no'} eq $no ) {									#<<<�ҏW�Ώۃf�[�^�̏ꍇ
			$ps =~ s/\n//;
			if ($FORM{'pass'} ne $password && (&pass_dec($ps))) {
				&fileunlock ;	#�t�@�C�����b�N����
				&error("�p�X���[�h���Ⴂ�܂��B");
			}
			if ( $FORM{'proc'} ne 'delete' )	{
				push(@new,"$no,$dt,$FORM{'name'},$FORM{$name_comment},$cnt,$FORM{'icon'},$FORM{'email'},$FORM{'hp'},$hst,$ps\n");			#�ҏW��̓��e�Œu��
			}	else	{
				if ( $logfile2 )	{
					if ( !(open(IN2,"$logfile2")))	{	&fileunlock ;	&error("���O�t�@�C���Q($logfile2)�̃I�[�v���Ɏ��s���܂���");	}
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
					if ( !(open(OUT,">$logfile2")))	{	&fileunlock ;	&error("���O�t�@�C��($logfile)�̃I�[�v���Ɏ��s���܂���");	}
					print OUT @sv;
					close(OUT);
				}
			}
		}	else	{										#<<<�ҏW�Ώۃf�[�^�ȊO�̏ꍇ
			$found = 0 ;
			if ( $FORM{'proc'} eq 'delete' ) {
				foreach $word ( @DELWORD )	{
					if ( $word && ( $no == $word ) ) {
						if ( $logfile2 )	{
							if ( !(open(IN2,"$logfile2")))	{	&fileunlock ;	&error("���O�t�@�C���Q($logfile2)�̃I�[�v���Ɏ��s���܂���");	}
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
							if ( !(open(OUT,">$logfile2")))	{	&fileunlock ;	&error("���O�t�@�C��($logfile)�̃I�[�v���Ɏ��s���܂���");	}
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
	if ( !(open(OUT,">$logfile")))	{	&fileunlock ;	&error("���O�t�@�C��($logfile)�̃I�[�v���Ɏ��s���܂���");	}
	print OUT @new;
	close(OUT);

	&fileunlock ;	#�t�@�C�����b�N����
	if ( $damedame == 0 )	{
		print "Location: $script?\n\n";
	}	else	{
		print "Content-type: text/html\n\n";
		print "<html><head><META HTTP-EQUIV=\"Refresh\" CONTENT=\"0; URL=";
		print "$script?\">";
		print $dmy_tok2_cookie; # �N�b�L�[�̔���
		print "</head><body></body></html>\n\n";
	}

}
###<--------------------------------------------------------------
###<---   ���K�җp���b�Z�[�W�t�@�C���X�V
###<--------------------------------------------------------------
sub update2 {
	&filelock ;		#�t�@�C�����b�N
	@MSGTBL = split(/\r/,$FORM{'msg'});
	foreach $buf ( @MSGTBL )	{	if ( $buf )	{	push(@MSGTBL2,$buf) ;	}	}
	if ( !(open(OUT,">$logfile3")))	{	&fileunlock ;	&error("���O�t�@�C��($logfile)�̃I�[�v���Ɏ��s���܂���");	}
	print OUT @MSGTBL2;
	close(OUT);

	&fileunlock ;	#�t�@�C�����b�N����
	if ( $damedame == 0 )	{
		print "Location: $script?\n\n";
	}	else	{
		print "Content-type: text/html\n\n";
		print "<html><head><META HTTP-EQUIV=\"Refresh\" CONTENT=\"0; URL=";
		print "$script?\">";
		print $dmy_tok2_cookie; # �N�b�L�[�̔���
		print "</head><body></body></html>\n\n";
	}

}
###<--------------------------------------------------------------
###<---   �����L���O�\��
###<--------------------------------------------------------------
sub ranking {
	if ( !(open(IN,"$logfile2")))	{	&error("���O�t�@�C���Q($logfile2)�̃I�[�v���Ɏ��s���܂���");	}
	@data = <IN>;
	close(IN);

	$totalcount = @data ;

	&header ;
	print "<a href=$script>�߂�</a><br>\n";

	@Lank = ();
    foreach $buf (@data) {
		($a,$b) = split(/,/,$buf);
		push(@Lank,"$b,$a");
	}
	@Lank = sort { $a <=> $b } @Lank ;
	@Lank = reverse @Lank ;
	print "<center>" if ( $acs == 0 ) ;
	print "<<<<< �����L���O >>>>><br><br>\n";
	$c = $totalcount - 1;
	print "�����e�Ґ�==>$c�l<br>\n";
	if ( $acs == 0 )	{
		print "<table border=0 width=50% cellspacing=3 cellpadding=5>\n";
		print "<td bgcolor=$cellheadbgcolor width=3% nowrap><font color=#ffffff>�����L���O</font></td>\n";
		print "<td bgcolor=$cellheadbgcolor width=70%><font color=#ffffff>�����O</font></td>\n";
		print "<td bgcolor=$cellheadbgcolor nowrap><font color=#ffffff>���e��</font></td>\n";
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
				print "<tr><td bgcolor=$bg><font color=$textcolor>��$cnt��</font></td>\n";
				print "<td bgcolor=$bg><font color=$textcolor>$nm</font></td>\n";
				print "<td bgcolor=$bg align=right><font color=$textcolor>$raihoucnt��</font></td>\n";
				print "<td bgcolor=$bg nowrap align=right><img src=\"$rankicon[$ranking]\"></td>\n" if ( $rankicon[$ranking] ) ;
				print "<td bgcolor=$bg width=2% nowrap align=right><font color=$textcolor>$rank[$ranking]</font></td>\n" if ( !($rankicon[$ranking]) ) ;
				print "</tr>\n";
			}	else	{
				print "��$cnt�ʁF$nm($raihoucnt��c$rank[$ranking])<br>";
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
###<---   Information(�A�C�R���ꗗ)
###<--------------------------------------------------------------
sub icondisp	{
	&header ;															#<<<html�w�b�_�[�o��
	print "<center><br><br>������ �A�C�R���ꗗ ������<br><br>\n";
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
		print "<br>����A�l��p�̃A�C�R���ł���<br><table cellpadding=5 cellspacing=0 border=0>\n";
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
	&footer ;															#<<<html�t�b�^�[�o��
	exit;
}
###<--------------------------------------------------------------
###<---   �G���[����
###<--------------------------------------------------------------
sub error {
	&header ;
	print "<font  color=\"$textcolor\">$_[0]</font>\n";
	&footer;
	exit;
}
###<--------------------------------------------------------------
###<---   �t�@�C�����b�N�ݒ�
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
	&error("�������̕����������ݒ��ł��B�u���E�U�́u�߂�v�Ŗ߂��čēx�o�^���s���ĉ������B");
}
###<--------------------------------------------------------------
###<---   �t�@�C�����b�N����
###<--------------------------------------------------------------
sub fileunlock {
	if (-e $lockfile) { unlink($lockfile); }
}
###<--------------------------------------------------------------
###<---   �A�C�R���\��
###<--------------------------------------------------------------
sub icon_set	{
	#��A�҂̓��e�̏ꍇ�A��A�җp�A�C�R���ɒu��������
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
###<---   ���O�_�E�����[�hi001112
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
	&header ;															#<<<html�w�b�_�[�o��
	print "<a href=$script>�߂�</a>\n";
	print "<center><font size=5><b><<< \��\�i���i >>></b></font><br><br>\n";
	print "�ȉ��̓��e�񐔂ɏ]���āA���Ȃ���\��\�i���Ă����܂�!!<br><br>\n";
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
			print "$OIWAI[$i]&nbsp;�`$j&nbsp;��\n";
		}	else	{
			print "$OIWAI[$i]&nbsp;�ȏ�\n";
		}
		print "</td>";
		print "<td nowrap bgcolor=#ffffff align=right><img src=\"$rankicon[$i]\"></td>\n" if ( $rankicon[$i] ) ;
		print "<td nowrap bgcolor=#ffffff align=right>&nbsp;</td>\n" if ( !($rankicon[$i]) ) ;
		print "</tr>\n";
		$i++;
	}
	print "</table></td></tr></table></center>";
	&footer ;															#<<<html�t�b�^�[�o��
	exit;
}
###<-------------------------------------------------------------
###<---   �����L���O�擾
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
###<---   �p�X���[�h�Í���
###<--------------------------------------------------------------
sub pass_enc {
	if ( $ango == 1 ) {
		$pass = crypt($_[0], $_[0]);
	}	else	{
		$pass = $_[0];
	}
}
###<-------------------------------------------------------------
###<---   �p�X���[�h�`�F�b�N
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
