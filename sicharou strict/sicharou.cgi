#!/usr/bin/perl
#�@��������������������̃T�[�o�[�̎d�l�ɍ��킹�ĕύX���ĂˁB
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++�@�@[ �������A������N!!  HTML 4.01 Strict Version ] �c ver1.1 (2003.9.7)
#+++	
#+++        �����>>> Edit by Noriya
#+++        Email    >>> pasokon-yugi@syd.odn.ne.jp
#+++�@�@�@�@Homepage >>> http://pasokon-yugi.cool.ne.jp/
#+++
#+++		�����>>> Original Script Created by Tacky				     
#+++
#+++		�����>>> Copyright (c) 1999.6 Tacky's Room. All rights reserved....
#+++
#+++        Email    >>> tacky2@ops.dti.ne.jp
#+++        Homepage >>> http://tackysroom.com/
#+++
#+++ �ݒu���@�\��(��̗�)
#+++
#+++ public_html�i�z�[���y�[�W�f�B���N�g���j
#+++ |
#+++ |-- cgi-bin�i�C�ӂ̃f�B���N�g���j
#+++      |-- credit�i�A�C�R���������Ă���f�B���N�g��,755�j
#+++  �@�@|-- yakushoku�i�A�C�R���������Ă���f�B���N�g��,755�j
#+++   �@ |-- jcode.pl      (755)�c(���{�ꃉ�C�u����)
#+++  �@�@|-- sicharou.cgi  (755)�c(�X�N���v�g�{��)
#+++   �@ |-- sicharou.txt  (666)�c(���O�t�@�C��)
#+++   �@ |-- sicharou2.txt (666)�c(���e�񐔊Ǘ��t�@�C��)
#+++  �@�@|-- sicharou3.txt (666)�c(��A�l�p���b�Z�[�W�i�[�t�@�C��)
#+++      |-- orange.gif    (644)�c(�w�i�̉摜�t�@�C���j
#+++      |-- sicharou.gif  (644)�c(�^�C�g���摜�t�@�C���j
#+++ �@�@���@( )���̐����̓p�[�~�b�b�V�����̒l�ł��B�@��
#+++
#+++        �摜�t�@�C���̓o�C�i�����[�h�i�p�[�~�b�V�����͂��ׂ�644�j�A����ȊO�̓A�X�L�[���[�h��FTP�]�����Ă��������B
#+++�@�@�@�@�摜�t�@�C���͍D���Ȃ��̂��g�����B�����ȑf�ޔz�z�T�C�g�֖K��Ă݂悤��
#+++
#+++ >>> Original Script Update-History...
#+++
#+++    2001.06.12(Ver0.981) >>  �����̓t�H�[���̔w�i�F���w�肵���ꍇ�A���O���ɔw�i�F�����Ȃ��s��C��
#+++    2001.03.12(Ver0.98)  >>  �����j���J�E���g�@�\�ɏ��i�@�\��t���܂����B�A�C�R���t�����i���\�ɂȂ�܂����B
#+++                             ��Location�w�b�_�[���g���Ȃ��T�[�o�[�̑Ή��B
#+++    2000.12.22(Ver0.974) >>  ���Ǘ��lү���ނ̐ݒ���@�̕��̓~�X�B(^^�U
#+++    2000.12.20(Ver0.973) >>  ���o�[�W�����A�b�v�����ꍇ�A�A�����e�񐔃G���[�ɂЂ������鎖������̂őΏ����܂���
#+++    2000.12.15(Ver0.972) >>  ���A�����e�񐔂ɒB���ĂȂ��̂ɃG���[�ɂȂ�ꍇ���������E�E�E(^-^;
#+++    2000.12.09(Ver0.971) >>  ���A�����e�G���[�ɂȂ����ꍇ�ł����e�񐔂��J�E���g�����s��C��
#+++    2000.11.29(Ver0.97)  >>  ��imode�Ή�
#+++                             ���Ǘ��l�A�C�R���E��A�A�C�R���ݒ�o�����I
#+++                             ���L�O�J�E���g�ɂ�邨�j�����b�Z�[�W���\���o�����I
#+++    2000.07.14(Ver0.96)  >>  �����L���O�\��������FORM�J�n�^�O�������Ă����E$footer�ƕ\������Ă��鎖���������E�P�s�e�L�X�g�̏ꍇCSS�����f����Ȃ�����
#+++    2000.07.12(Ver0.95)  >>  ̧��ۯ�����������Ȃ��ꍇ������s��C��
#+++	2000.06.21(Ver0.94)  >>�@�ٱ��&URL���w�肵�Ȃ��ݒ�������submit�{�^�����Q�\������Ă��܂����B�Etextcolor�̐ݒ肪�Ԉ���Ă܂���
#+++	2000.06.13  >>�@Apache+Netscape���������Ή��E�ٱ��,URL�̎w��ǉ��E����÷�đΉ��E[name]�ɔ��p��߰�������Ɣ��p��߰��ȍ~�F�����Ȃ��޸ޏC��
#+++�@�@�@�@�@�@�@�@�@�@�t�H���g�T�C�Y�w��\�ɂ��܂����ECSS�ǉ��E���b�N����������
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

##########################
## �ȉ��A�ݒ荀�ڂł��B ##
##########################

require './jcode.pl';										#���{��R�[�h�ϊ�
$script 			= "./sicharou.cgi";						#<<<���̃X�N���v�g�̖��O

$URL                = "http://�`";                                     #<<<���̃X�N���v�g�̐��URL�B�����������Ə����Ă����ƁA�y�[�W��ԉ��̃����N�uW3C MarkUp Validation Service�v����A����CGI���f���o��HTML��W3C�W���d�l�ɏ������Ă��邱�Ƃ��m�F�ł��܂��i�΁j�B�܂��A��̐��E�Ƃ������ƂŁc�B

$method 			= "POST";								#<<<METHOD�̎w��iPOST�œ��삵�Ȃ�������AGET)
$logfile 			= "./sicharou.txt";						#<<<���b�Z�[�W�̃��O�t�@�C����
$logfile2 			= "./sicharou2.txt";					#<<<���b�Z�[�W��o�^���Ă��ꂽ���̓o�^�񐔗݌v��ێ�����t�@�C��
$logfile3 			= './sicharou3.txt';					#<<<���b�Z�[�W��o�^���Ă��ꂽ���X�ւ̐l�ʃ��b�Z�[�W��o�^����t�@�C��
$lockfile			= './sicharou.lock';					#<<<���b�N�t�@�C���̖��O���w��
$title  			= "���A������N";					#<<<�^�C�g�����w��
$titlelogo 			= "sicharou.gif";		#<<<��i���Ƀ^�C�g�����S���w�肷��ꍇ�A�t���p�X�Ŏw��B�w�肵�Ȃ��ꍇ�́u""�v
$title_w			= "300";					#<<<�^�C�g�����S�̉����i�s�N�Z���j
$title_h			= "50";					#<<<�^�C�g�����S�̍����i�s�N�Z���j
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
$textflg_i			= 1 ;									#<<<���b�Z�[�W���̌`��B�i1:�P�s�e�L�X�g�@2:�����s�e�L�X�g�j
$emailflg_i			= 1 ;									#<<<���[���A�h���X����͂���H(0:���Ȃ� 1:����)
$hpflg_i			= 1 ;									#<<<�t�q�k����͂���H(0:���Ȃ� 1:����)


#(Web�̏ꍇ)
$w_name_sz			= 20 ;									#<<<���O���̕�����
$w_email_sz			= 35 ;									#<<<Email���̕�����
$w_hp_sz			= 35 ;									#<<<Homepage���̕�����
$w_message_sz1		= 32 ;									#<<<���b�Z�[�W���̕�����
$w_message_sz2		= 5 ;									#<<<���b�Z�[�W���̍s�����P�s�e�L�X�g�̏ꍇ�͑ΏۊO
$pagemax 			= 20 ;									#<<<�P�y�[�W���ɕ\�����錏��
$textflg			= 2 ;									#<<<���b�Z�[�W���̌`��B�i1:�P�s�e�L�X�g�@2:�����s�e�L�X�g�j
$emailflg			= 1 ;									#<<<���[���A�h���X����͂���H(0:���Ȃ� 1:����)
$hpflg				= 1 ;									#<<<�t�q�k����͂���H(0:���Ȃ� 1:����)
#####################################
$line1 		= "line1";
$line2 		= "line2";
#============================================================================================================================================
$url 				= "http://�`";				#<<<�߂���URL�i�ʏ�͂��Ȃ��̃T�C�g�̃g�b�v�y�[�WURL�j
$password 			= "password";						#<<<�Ǘ��҃����e�i���X�p�p�X���[�h�i���O�ҏW�p�j�j
$kanriname			= "�Ǘ��l�̖��O";								#<<<�f���Ǘ��҂̖��O�i�����Ɏw�肳�ꂽ���O�́A�����L���O�ΏۊO�ƂȂ�܂��j
$datamax 			= 200 ;									#<<<�ő�f�[�^�ۑ�����
$messagemax 		= 50 ;									#<<<���K�җp���b�Z�[�W�̍ő匏��
$manual 			= 2 ;									#<<<�Ǘ��l����̃��b�Z�[�W��\������H(0:no 1:����̫�т̉��ɕ\�� 2:��ʉ����ɕ\��)

#���A�C�R���̎w��B$icon_gif[3]...[10]�̂悤�ɓK���ɑ��₵�ĉ������ˁB	��imode�ł̓A�C�R���͕\���o���܂���
$icon_flg			= 'yes';								#���e���ɃA�C�R�����g�p���邩�H�g�p����ꍇ��'yes'�Ɠ��͂���
#���Ǘ��җp�A�C�R���ƃp�X���[�h���w��B�Ǘ��l�͂P�����A�C�R���o�^�o���܂���B
#  $oiconnm�Ɏw�肵�����O�œ��e�����ꍇ�A$oicon_gif�̃A�C�R�����\�������悤�ɂȂ��Ă��܂��B
#���̉��́A�摜�T�C�Y�B_w�͕��i�s�N�Z���j�B_h�͍����i�s�N�Z���j�ł��B�킩��Ȃ��ꍇ��_w�̕�����0�ɂ��Ă����ĂˁB
#�Ǘ��҃A�C�R���͓��ɕK�v�����ꍇ�́A$oicon_gif = '';�Ƃ��ĉ������B
$oicon_gif	  = 'credit/jcb.gif' ;		$oiconnm  = '�Ǘ��l';
$oicon_gif_w = 32 ; $oicon_gif_h = 32 ; 

#����A�җp�A�C�R���Ɠ��e���̖��O���w��B�ǉ�����������$jicon_gif[2]...[5]�̂悤�ɑ��₵�ĉ������ˁB
#  $jiconnm�Ɏw�肵�����O�œ��e�����ꍇ�A$jicon_gif�̃A�C�R�����\�������悤�ɂȂ��Ă܂��B
#���̉��́A�摜�T�C�Y�B_w�͕��B_h�͍����ł��B$jicon_gif���A�C�R���t�@�C����URL $jiconnm�������O $jicon_gif w���A�C�R���̕��i�s�N�Z���j $jicon_gif_h���A�C�R���̍����i�s�N�Z���j

$jicon_gif[0] = 'credit/jcb.gif' ;		$jiconnm[0] = '�Ǘ��l' ;
$jicon_gif_w[0] = 32 ; $jicon_gif_h[0] = 32 ;

#�����@[]���̐�����ς���΂����ł��o�^�ł��܂��B����1�Ԃ��g�����́A�擪��#���O���Ă����p�������B 
#$jicon_gif[1] = '' ;	$jiconnm[1] = '';
#$jicon_gif_w[1] = 32 ; $jicon_gif_h[1] = 32 ; 

$icon_imode			= 7	;
#imode����̃A�N�Z�X�̏ꍇ�A�Œ�łP�������L�̃A�C�R���̔ԍ���I�����Ă��������B

#�K��җp�A�C�R���ƃA�C�R���̖��O�̎w��B$icon_gif[3]...[10]�̂悤�ɓK���ɑ��₵�ĉ������ˁB
#���̉��́A�摜�T�C�Y�B_w�͕��B_h�͍����ł��B

$icon_gif[0] = 'credit/amex.gif' ;		$iconnm[0] = '�A���b�N�X' ;
$icon_gif_w[0] = 32 ; $icon_gif_h[0] = 32 ; 
$icon_gif[1] = 'credit/aplus.gif' ;		$iconnm[1] = '�A�v���X' ;
$icon_gif_w[1] = 32 ; $icon_gif_h[1] = 32 ;
$icon_gif[2] = 'credit/cf.gif' ;		$iconnm[2] = 'CF�J�[�h' ;
$icon_gif_w[2] = 32 ; $icon_gif_h[2] = 32 ;
$icon_gif[3] = 'credit/aeon.gif' ;	$iconnm[3] = '�C�[�I��' ;
$icon_gif_w[3] = 32 ; $icon_gif_h[3] = 32 ;
$icon_gif[4] = 'credit/acom.gif' ;	$iconnm[4] = '�A�R��' ;
$icon_gif_w[4] = 32 ; $icon_gif_h[4] = 32 ;
$icon_gif[5] = 'credit/dc.gif' ;		$iconnm[5] = 'DC�J�[�h' ;
$icon_gif_w[5] = 32 ; $icon_gif_h[5] = 32 ;
$icon_gif[6] = 'credit/aiful.gif' ;	$iconnm[6] = '�A�C�t��' ;
$icon_gif_w[6] = 32 ; $icon_gif_h[6] = 32 ;
$icon_gif[7] = 'credit/dic.gif' ;	$iconnm[7] = '�f�B�b�N' ;
$icon_gif_w[7] = 32 ; $icon_gif_h[7] = 32 ;
$icon_gif[8] = 'credit/jaccs.gif' ;	$iconnm[8] = '�W���b�N�X' ;
$icon_gif_w[8] = 32 ; $icon_gif_h[8] = 32 ;
$icon_gif[9] = 'credit/jcb.gif' ;	$iconnm[9] = 'JCB' ;
$icon_gif_w[9] = 32 ; $icon_gif_h[9] = 32 ;
$icon_gif[10] = 'credit/lake.gif' ;	$iconnm[10] = '���C�N' ;
$icon_gif_w[10] = 32 ; $icon_gif_h[10] = 32 ;
$icon_gif[11] = 'credit/master.gif' ;	$iconnm[11] = '�}�X�^�[' ;
$icon_gif_w[11] = 32 ; $icon_gif_h[11] = 32 ;
$icon_gif[12] = 'credit/million.gif' ;	$iconnm[12] = '�~���I��' ;
$icon_gif_w[12] = 32 ; $icon_gif_h[12] = 32 ;
$icon_gif[13] = 'credit/nicos.gif' ;		$iconnm[13] = '�j�R�X' ;
$icon_gif_w[13] = 32 ; $icon_gif_h[13] = 32 ;
$icon_gif[14] = 'credit/visa.gif' ;	$iconnm[14] = 'VISA' ;
$icon_gif_w[14] = 32 ; $icon_gif_h[14] = 32 ;
$icon_gif[15] = 'credit/orico.gif' ;	$iconnm[15] = '�I���R' ;
$icon_gif_w[15] = 32 ; $icon_gif_h[15] = 32 ;
$icon_gif[16] = 'credit/orix.gif' ;	$iconnm[16] = '�I���b�N�X' ;
$icon_gif_w[16] = 32 ; $icon_gif_h[16] = 32 ;
$icon_gif[17] = 'credit/promise.gif' ;	$iconnm[17] = '�v���~�X' ;
$icon_gif_w[17] = 32 ; $icon_gif_h[17] = 32 ;
$icon_gif[18] = 'credit/saison.gif' ;		$iconnm[18] = '�Z�]��' ;
$icon_gif_w[18] = 32 ; $icon_gif_h[18] = 32 ;
$icon_gif[19] = 'credit/uc.gif' ;		$iconnm[19] = 'UC�J�[�h' ;
$icon_gif_w[19] = 32 ; $icon_gif_h[19] = 32 ;

#�A�C�R���ꗗ��\������ہA�P�s�ɃA�C�R�������\�����܂��H
$icon_line					= 5 ;	#���̏ꍇ�A5�\����������s������Ď��ł��B

#<<<Web����̃A�N�Z�X���A��ʉ����ɕ\������u�Ǘ��l����̃��b�Z�[�W�v�B"EOM"�`EOM�̍s�܂łɕK������Ă��������B���b�Z�[�W�s�v�̏ꍇ�́A$manualmsg�̍s����EOM�̍s�܂őS�č폜���Ă�
$manualmsg = <<"EOM";
<p class="setsumei">���͂���΁[�I�l�u������N�v�͉�����\�\\���܂��ƁA�R�~���j�P�[�V�������Ƃ�ׂɂƂ��Ă���؂Ȏ��A����!!�w���A�x�ł�!!....���A���܂���`�I�������ꂾ���B�i�΁j �l�̎g�����́u���O�������āA�|����@�����������`��v�Ł`���B</p>

<p class="setsumei">���⑫�F�w���͂���΁`��x�́A�݂Ȃ��񂪂����A���Ă���邩�킩��Ȃ�����A�u���͂悤�v�A�u����ɂ��́v�A�u����΂��v���~�b�N�X���Ă݂܂����`��i�΁j iMode�ł������܂��B�i���Ԃ�c�j</p>
EOM

#<<<imode����̃A�N�Z�X���A��ʉ����ɕ\������Ǘ��҂���̃��b�Z�[�W�B"EOM"�`EOM�̍s�܂łɕK������Ă��������B���b�Z�[�W�s�v�̏ꍇ�́A$manualmsg2�̍s����EOM�̍s�܂őS�č폜���Ă�
$manualmsg2 = <<"EOM";
<p>�݂�ȋC�y�ɏ������݂��Ăˁ`��</p>
EOM

@errtag = ('table','meta','form','!--','embed','html','body','tr','td','th','a');		#�f���W�����`�ȃ^�O

#=============================================================================================================================================================================================

$rankcnt					= 30 ;	#�����L���O��ʉ��l�������L���O�ꗗ��ʂɕ\�����܂����H

#���j���J�E���g�ݒ�B�w�肵�����e�񐔂ɒB����ƁA���j�����b�Z�[�W��\�����܂��B�s�v�̏ꍇ�́A@OIWAI�̍s���폜���ĂˁB

@OIWAI = (0,10,30,50,80,120,170,230,300,400,600,1000,1500,2500,4000);

#���j�����b�Z�[�W�\���̍ۂ̕��́BNAME��CNT�̕����ɂ͂��̐l�̖��O�ƒB���񐔂��u������܂��̂ŁA
#�K��NAME�ECNT�Ƃ��������͓���Ă����Ă��������B

$oiwaimsg = "NAME����!! ���e�񐔂�CNT��ɒB�������i���܂���!!!!!";

#�f���r�炵�΍�B�r���������v���o�̃A�h���X��ݒ肵�ĉ������B
#�@"xxx?.com"�Ƃ����ꍇ�A"xxx1.com","xxx2.com"���A�u�H�v�̕�����������P�Ɣ��f���܂�
#  "xxx*.com"�Ƃ����ꍇ�A"xxx1.com","xxx12345.com���A�u���v�̕������O�ȏ�̕�����Ɣ��f���܂��B
#��F@DANGER_LIST=("xxx.com","yyy.com","zzz*.or.jp");

@DANGER_LIST=("","","");

#�f���r�炵�΍􂻂̂Q�B���b�Z�[�W�ő啶�������w��B���ɐݒ肵�Ȃ��ꍇ�́A''�Ƃ��ĉ������B

$maxword = '1000' ;

$renchan1		= 1 ;		#�w�蕪�ȓ��̘A�����e�ʹװ�Ƃ���B�ݒ肵�Ȃ��ꍇ��0�Ƃ��ĂˁB
$renchan2		= 4 ;		#�w��񐔈ȏ�̘A�����e�ʹװ�Ƃ���B�ݒ肵�Ȃ��ꍇ��0�Ƃ��ĂˁB

$method 			= "POST";								#<<<METHOD�̎w��iPOST�œ��삵�Ȃ�������AGET)

#����L�ɂ���u@OIWAI�v�Ɏw�肵���񐔂ŏ��i���Ă����܂��B@OIWAI�Ɠ��������ݒ肵�ĉ������B
@rank	= ('�c�t����','���w�Z��w�N','���w�Z���w�N','���w�Z���w�N','���w��','���Z��','��w��','���Ј�','�W��','�ے�','����','�햱','�ꖱ','�В�','�');

#�����i�ɉ摜���g���ꍇ�A���i�񐔂Ɠ��������ݒ肵�Ă��������B��$rankicon[n]�͕K���u0�v����n�܂�܂��B�摜���g��Ȃ�������''�Ƃ��ĂˁB
#�@�摜�̕��E�������킩��Ȃ��l�́A$rankicon_w[n] = 0 ; $rankicon_h[n] = 0 ;�̂悤�Ɂu0�v�Ƃ��ĉ������B

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

$damedame		= 0 ;	#Location�w�b�_���g���Ȃ��T�[�o�[��1�B�ʏ��0�ł����͂��B���g�N�g�N�A3nopage,WinNT�T�[�o�[����1���ȁB

#####################################################
##                                                 ##
##�@�������牺�͂�����Ȃ������g�̂��߂ł��B(^_^;  ##
##                                                 ##
#####################################################

utime time(), time(), __FILE__; 								# �X�N���v�g���������̍X�V

#������Web����̃A�N�Z�X���炩iMODE����̃A�N�Z�X���𔻒f
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
if ($ENV{'HTTP_USER_AGENT'} !~ /MSIE/i || $acs == 1 ) { $css_style = "" ; }		#Netscape-CSS�Ή�

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

if ($ENV{'HTTP_USER_AGENT'} !~ /MSIE/i) {	$css_style = "" ;	}		

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
		}
		&dataread ;
	}
	&header ;						   			#<<<html�w�b�_�[�̏o��
	&inputform ; 				       			#<<<���̓t�H�[���̕\��
	&disp ;							   			#<<<�o�^�σ��b�Z�[�W�̕\��
	if ( $manual == 2 )	{	&setumei;	}	#<<<�u�g�����v�̕\��
	print "\n<form action=\"$script\" method=\"$method\">\n";
	print "<dl class=\"password\">\n";
	if ( $acs == 0 ) { print "<dt>No</dt>\n";	}
	print "<dd><input type=\"text\" name=\"no\" size=\"4\"></dd>\n";
	if ( $acs == 1 ) { print "<dt>No</dt>\n";	}
	if ( $acs == 0 ) { print "<dt>Pass</dt>\n";	}
	print "<dd><input type=\"password\" name=\"pass\" size=\"8\"></dd>\n";
	if ( $acs == 1 ) { print "<dt>Pass</dt>\n";	}
	print "<dt><select name=\"proc\">\n";
	print "<option value=\"edit\">�ҏW\n";
	print "<option value=\"delete\">�폜\n";
	print "<option value=\"message\">�K��҃��b�Z�[�W\n";
	print "</select>\n</dt>\n";
	if ( $acs == 1 ) { print "";	}
	print "<dd><input type=\"hidden\" name=\"action\" value=\"maintenance\">\n";
	print "<input type=\"submit\" value=\"ADMIN\"></dd>\n</dl>\n";
	#<<<�@�������Ȃ��Ńl��
	print "<ul class=\"ScriptAuthor\">\n<li><a href=\"http://tackysroom.com/\">sicharou(Ver0.981)-Tacky</a></li>\n<li>Edit by <a href=\"http://pasokon-yugi.cool.ne.jp/\">Noriya@�ς�����䂤��</a></li>\n";
    print "<li><a href=\"http://validator.w3.org/check?uri=$URL\">W3C MarkUp Validation Service</a></li>\n</ul>\n";
	print "</form>\n\n";
	print "" if ( $acs == 0 );	
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
		read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
	} else { $buffer = $ENV{'QUERY_STRING'}; }
	@pairs = split(/&/,$buffer);
	@msg = ();
	foreach $pair (@pairs) {
		($name, $value) = split(/=/, $pair);
		$value =~ tr/+/ /;
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		foreach ( @errtag )	{
			if ($value =~ /<$_(.|\n)*>/i) {	 &error("�g�p�o���Ȃ��^�O�����͂���Ă��܂�");	}
		}
		$value =~ s/\,/�C/g;
		&jcode'convert(*value,'sjis');
		$FORM{$name} = $value;
	}
	$FORM{'com'} =~ s/\r\n/<br>/g;	$FORM{'com'} =~ s/\r|\n/<br>/g;	
	$FORM{'hp'}   =~ s/^http\:\/\///;
	if ( $acs == 1 )	{	$FORM{'icon'} = $icon_imode ;	}
}
###<--------------------------------------------------------------
###<---   HTML�w�b�_�[�����o��
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
###<---   HTML�t�b�_�[�����o��
###<--------------------------------------------------------------
sub footer { 
	print "</body>\n</html>\n";
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
###<---   ���̓t�H�[��
###<--------------------------------------------------------------
sub	inputform	{
	if ( $acs == 0 )	{
		print "<form action=\"$script\">\n";
		print "<ul class=\"navi\">\n";
		print "<li><input type=\"button\" VALUE=\"HOME\" ";
		print "onClick=\"parent.location.href=\'$url\'\"></li>\n";
		if ( $logfile2 && $FORM{'action'} ne 'download')	{	#i001112
#			print "<form>\n";	#i000714
			print "<li><INPUT TYPE=\"button\" VALUE=\"�����L���O\" ";
			print "onClick=\"parent.location.href=\'$script?action=ranking\'\"></li>\n";
		}
		if ( $logfile2 && $FORM{'action'} ne 'download')	{
#			print "<form>\n";
			print "<li><INPUT TYPE=button VALUE=\"���i���i����\" ";
			print "onClick=\"parent.location.href=\'$script?action=info\'\"></li>\n";
		}
		print "</ul>\n</form>\n\n";
	}	else	{
		if ( $url )	{	print "<ul>\n<li><a href=\"$url\">HOME</a></li>\n";	}
		if ( $logfile2 && $FORM{'action'} ne 'download')	{	#i001112
			print "<li><a href=\"$script?action=ranking\">�����L���O</a></li>\n";
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
#�ʏ�E�F�u�T�C�g�Ȃ��
	if ( $acs == 0 )	{
#$textflg��������
	if ( $textflg != 1 )	{
		#�������O
		print "<div class=\"input\">\n<dl>\n<dt>Name</dt>\n";
		print "<dd><input type=\"text\" name=\"name\" size=\"$name_sz\" value=\"$c_name\"></dd>\n";
#���A�C�R��
		if ( $icon_flg eq 'yes' )	{
			print "<dt>Icon</dt>\n<dd><select name=\"icon\">\n";
			for ( $i = 0 ; $i <= $#iconnm ; $i++ ) {
				if ( $i == $c_icon )	{	$dmy = "selected";	}	else	{	$dmy = "" ;	} 
				print "<option value=\"$i\">$iconnm[$i]</option>\n";
			}
#���A�C�R�������܂�
			print "</select></dd>\n";
		}
#$textflg�����܂�
		if ( $emailflg == 1 ) { 
			#�����[���A�h���X
			print "<dt>Email</dt>\n<dd><input type=\"text\" name=\"email\" size=\"$email_sz\" value=\"$c_email\"></dd>\n";
		}
		if ( $hpflg == 1 ) { 
			#��Homepage
			print "<dt>URL</dt>\n<dd><input type=\"text\" name=\"hp\" size=\"$hp_sz\" value=\"http://$c_hp\"></dd>\n";
		}
		print "<dt>Comment</dt>\n";
		print "<dd><textarea name=\"com\" cols=\"$message_sz1\" rows=\"$message_sz2\">$c_cm</textarea></dd>\n</dl>\n";
		print "<ul id=\"submit\">\n<li><input type=\"submit\" value=\"$submit\"></li>\n";
		if ( $icon_flg eq 'yes' )	{	print "<li><a href=\"$script?action=icondisp\">�A�C�R���ꗗ</a></li>\n</ul>\n</div>\n";	}

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
				print "<li><a href=\"$script?action=icondisp\">�A�C�R���ꗗ</a>";
			}

		print "</ul>\n</div>\n\n";

	}
	}	else	{		#imode��
		#�������O
		print "<dl>\n<dt>Name</dt>";
		print "<dd><input type=\"text\" name=\"name\" size=\"$name_sz\" value=\"$c_name\"></dd>\n";
		if ( $emailflg == 1 ) { 
			#�����[���A�h���X
			print "<dt>Email</dt>\n<dd><input type=\"text\" name=\"email\" size=\"$email_sz\" value=\"$c_email\"></dd>\n";
		}
		if ( $hpflg == 1 ) { 
			#��Homepage
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

	if ( $manual == 1 )	{	&setumei;	}	#<<<�u�g�����v�̕\��

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
###<---   �݂Ȃ��񂩂�̈��A��\��
###<--------------------------------------------------------------
sub	disp	{

	if ( $acs == 0 )	{
		print "<h1>$title</h1>\n" if ( $FORM{'action'} eq 'download' ) ;;
		if ( !(open(IN3,"$logfile3")))	{	&error("���O�t�@�C���R($logfile3)�̃I�[�v���Ɏ��s���܂���");	}
		@message = <IN3>;
		close(IN3);
		foreach ( @message ) {
			($n,$m) = split(/:/,$_);
			if ( $c_name eq $n )	{
				print "<div class=\"adminmessage\">\n<h2>�Ǘ��l����̃��b�Z�[�W</h2>\n<p>\n$m</p>\n</div>\n\n";
			}
		}
		print "<table summary=\"�F����̂����A\">\n";
		print "<caption>�F����̂����A�ꗗ</caption>\n";
		print "<tr class=\"header\">\n<th class=\"number\">No</th>\n";
		print "<th class=\"date\">Date</th>\n";
		print "<th class=\"name\">Name</th>\n";
		if ( $icon_flg eq 'yes' && $FORM{'action'} ne 'download' )	{
			print "<th class=\"icon\">Icon</th>\n";
		}
		if ( $hpflg == 1 )	{	print "<th class=\"url\">Site</th>\n";	}
		print "<th class=\"message\">Message</th>\n";
		if ( $logfile2 )	{
			print "<th class=\"kaisu\">��</th>\n";
			print "<th class=\"shoshin\">��E</th>\n";
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
				if ( $cm eq '' ) {	$cm = '�@';	}
				print "<td class=\"message\">$cm</td>\n";
				if ( $logfile2 )	{	#i001112
					print "<td class=\"kaisu\">$raihoucnt</td>\n";
					$ranking = &rankget($raihoucnt) ;
					print "<td class=\"shoshin\">";
					print "<img src=\"$rankicon[$ranking]\" alt=\"��E\" width=\"$rankicon_w[$ranking]\" height=\"$rankicon_h[$ranking]\">\n" if ( $rankicon[$ranking] ) ;
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
				print "($raihoucnt��c$rank[$ranking])\n";
			}
			if ( $hpflg == 1 )	{
				if ( $hp )	{	print "<a href=\"http://$hp\">-[URL]</a>\n";	}
			}
			print "";
			if ( $cm eq '' ) {	$cm = '�@';	}
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
			print "<p class=\"totalcount\">TotalCount�́A���Ȃ��̉ߋ�����̈��A�񐔂ł���</p>\n\n";
		}
	}	else	{
		print "<p>( )�̐����͓��e�񐔂ł�</p>\n";
	}
	if ( $acs == 0 )	{	#i001112
		print "" ;
		print "<form action=\"$script\" method=\"$method\" class=\"logdownload\">\n";
		print "<ul class=\"download\">\n<li><input type=\"hidden\" name=\"action\" value=\"download\">\n";
		print "<input type=\"submit\" value=\"���O���_�E�����[�h\"></li>\n</ul>\n";
		print "<p class=\"caution\">�_�E�����[�h�����t�@�C���̊g���q�� .cgi �� .html �ɕύX���ĉ������ˁ�</p>\n";
		print "</form>\n";
	}
}
###<--------------------------------------------------------------
###<---   ���A���O�o��
###<--------------------------------------------------------------
sub	regist	{
	if ( $FORM{'name'} eq "")	{	&error("���O�͏ȗ��o���܂���B") ;	}
	if ( $maxword ne '' && (length($FORM{'com'}) > $maxword))	{	&error("���b�Z�[�W��$maxword�����܂ł����o�^�o���܂���B");	}
	if ( $textflg2 == 1 && $FORM{'com'} eq '' )	{	&error("���b�Z�[�W���͏ȗ��o���܂���B") ;	}

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
			if($host =~ /$buf/gi){	&error("\�\\��\�󂠂�܂���B<br>���Ȃ��̃v���o�C�_�[����͓��e�ł��܂���ł����B");	}
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
	$cook="nm\!$FORM{'name'},icon\!$FORM{'icon'},em\!$FORM{'email'},hp\!$FORM{'hp'}";
	print "Set-Cookie: sicharou=$cook; expires=$date_gmt\n";
}
###<--------------------------------------------------------------
###<---   �����e�i���X���[�h
###<--------------------------------------------------------------
sub Maintenance {
	if ( $FORM{'proc'} ne 'message' && $FORM{'no'} eq "")	{	&error("�����e�i���X�Ώۂ̋L��No���w�肵�ĉ������B");	}
	if ( $FORM{'pass'} eq "")	{	&error("�p�X���[�h����͂��ĉ������B");	}
	if ( $FORM{'pass'} ne $password)	{	&error("�p�X���[�h���Ⴂ�܂��B") ;	}

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
	print "<ul class=\"back\">\n<li><a href=\"$script\">BACK</a></li>\n</ul>\n";
if ( $acs == 0 )	{
print <<"EOM";
<h1>�����K�Җ��ɓ���̃��b�Z�[�W��\\������ݒ聡</h1>

<p>���K�҂��N�b�L�[�������Ă���ꍇ�A�����œo�^�������O�̐l���A�N�Z�X�����ۂɐݒ肵�����b�Z�[�W���\\������܂��B</p>

<p>�ݒ���@�́A�u�K��҂̖��O�v+�u:�i���p�R�����j�v�{�u�\\�����b�Z�[�W�v�{�u���s�v�ł���l�l�̃��b�Z�[�W�ƂȂ�܂��B</p>

<p>���͂̓r���ŉ��s�����ꍇ�̓��b�Z�[�W��&lt;br&gt;�����Đݒ肵�ĉ������B</p>

<dl>
<dt>��F</dt>
<dd>�`����:�������Ă���Ă��肪�Ƃ�</dd>
<dd>�a����:���΂炭���ĂȂ��˂��E�E�E</dd>
<dd>�b����:�b����ցI&lt;em&gt;�a�������߂łƁ[!!!&lt;/em&gt;</dd>
<dd>���^�O��}���\\�ł��B</dd>
</dl>
EOM
}	else	{
print <<"EOM";
<h1>�����K�Җ��̃��b�Z�[�W�ݒ聡</h1>

<p>�u�K��҂̖��O�v+�u:�i���p�R�����j�v�{�u�\\�����b�Z�[�W�v�{�u���s�v�ł���l�l�̃��b�Z�[�W�ƂȂ�܂��B</p>

<p>���͂̓r���ŉ��s�����ꍇ�̓��b�Z�[�W��&lt;br&gt;�����Đݒ肵�ĉ������B</p>
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
		print "<dd><input type=\"submit\" value=\"�K��҃��b�Z�[�W���X�V����\"></dd>\n</dl>\n";
		print "</form>\n";
	}	else	{
		print "<textarea name=\"msg\" cols=\"$message_sz1\" rows=\"$message_sz2\">$BUF</textarea>\n";
		print "<input type=\"submit\" value=\"�X�V\">\n";
		print "</form>\n";
	}
	&footer ;
	exit ;
}
###<--------------------------------------------------------------
###<---   ���O�t�@�C���X�V
###<--------------------------------------------------------------
sub update {

	&filelock ;		#�t�@�C�����b�N
	&dataread ;
    foreach (@LOG) {
		($no,$dt,$nm,$cm,$cnt,$icon,$email,$hp,$hst,$dmy) = split(/,/,$_);
        if ($FORM{'no'} eq $no ) {									#<<<�ҏW�Ώۃf�[�^�̏ꍇ
			if ( $FORM{'proc'} ne 'delete' )	{
				push(@new,"$no,$dt,$FORM{'name'},$FORM{'com'},$cnt,$FORM{'icon'},$FORM{'email'},$FORM{'hp'},$hst,$dmy");			#�ҏW��̓��e�Œu��
			}
		}	else	{										#<<<�ҏW�Ώۃf�[�^�ȊO�̏ꍇ
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
	print "<ul class=\"back\">\n<li><a href=\"$script\">�߂�</a></li>\n</ul>\n";

	@Lank = ();
    foreach $buf (@data) {
		($a,$b) = split(/,/,$buf);
		push(@Lank,"$b,$a");		
	}
	@Lank = sort { $a <=> $b } @Lank ;
	@Lank = reverse @Lank ;
	print "" if ( $acs == 0 ) ;
	print "<h1>&lt;&lt;&lt;&lt;&lt; �����L���O &gt;&gt;&gt;&gt;&gt;</h1>\n";
	$c = $totalcount ;
	print "<p class=\"tokoshasu\">�����e�Ґ�==&gt;$c�l</p>\n"; 
	if ( $acs == 0 )	{
		print "<table summary=\"���e�ҏ��\" class=\"ranking\">\n<tr class=\"header\">\n";
		print "<th>�����L���O</th>\n";
		print "<th>�����O</th>\n";
		print "<th>���e��</th>\n";
		print "<th>���i���</th>\n</tr>\n";
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
				print "<tr class=\"$bg\">\n<td>$cnt��</td>\n";
				print "<td>$nm</td>\n";
				print "<td>$raihoucnt��</td>\n";
				print "<td><img src=\"$rankicon[$ranking]\" alt=\"Ranking\" width=\"$rankicon_w[$ranking]\" height=\"$rankicon_h[$ranking]\"></td>\n" if ( $rankicon[$ranking] ) ;
				print "<td>$rank[$ranking]</td>\n" if ( !($rankicon[$ranking]) ) ;
				print "</tr>\n";
			}	else	{
				print "$cnt�ʁF$nm($raihoucnt��c$rank[$ranking])<br>";
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
###<---   Information(�A�C�R���ꗗ)
###<--------------------------------------------------------------
sub icondisp	{	
	&header ;															#<<<html�w�b�_�[�o��
	print "<ul class=\"back\">\n<li><a href=\"$script\">�߂�</a></li>\n</ul>\n";
	print "<h1>������ �A�C�R���ꗗ ������</h1>\n";
	print "<table cellpadding=\"5\" cellspacing=\"0\" summary=\"�A�C�R���ꗗ\" class=\"iconlist\">\n";
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
		print "<h2>����A�l��p�̃A�C�R���ł���</h2>\n<table cellpadding=5 cellspacing=0 summary=\"��A�l��p�A�C�R��\" class=\"joren\">\n";
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
						print "<td>(�Ȃ�)</td>\n";
						print "<td>(�����)</td>\n";
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
	&footer ;															#<<<html�t�b�^�[�o��
	exit;
}
###<--------------------------------------------------------------
###<---   �G���[����
###<--------------------------------------------------------------
sub error {
	&header ;
	print "<ul class=\"back\">\n<li><a href=\"$script\">�߂�</a></li>\n</ul>\n";
	print "<p class=\"error\">$_[0]</p>\n";
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
###<---   ���O�_�E�����[�hi001112
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
	&header ;															#<<<html�w�b�_�[�o��
	print "<ul class=\"back\">\n<li><a href=\"$script\">�߂�</a></li>\n</ul>\n";
	print "<h1>&lt;&lt;&lt; \��\�i���i &gt;&gt;&gt;</h1>\n";
	print "<p class=\"rule\">�ȉ��̓��e�񐔂ɏ]���āA���Ȃ���\��\�i���Ă����܂�!!</p>\n";
	$i =  0;
	print "<table cellpadding=5 cellspacing=1 summary=\"���i���i\" class=\"shoshinshikaku\">\n";
	print "<tr>\n";
	print "<th>���i</th>\n";
	print "<th>���e��</th>\n";
	print "<th>�A�C�R��</th>\n";
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
			print "$OIWAI[$i]&nbsp;�`$j&nbsp;��\n";
		}	else	{
			print "$OIWAI[$i]&nbsp;��ȏ�\n";
		}
		print "</td>\n";
		print "<td><img src=\"$rankicon[$i]\" alt=\"icon\" width=\"$rankicon_w[$i]\" height=\"$rankicon_h[$i]\"></td>\n" if ( $rankicon[$i] ) ;
		print "<td>�Ȃ�</td>\n" if ( !($rankicon[$i]) ) ;
		print "</tr>\n";
		$i++;
	}
	print "</table>\n";
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
