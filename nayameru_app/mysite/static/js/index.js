+$(function() {
	'use strict';

	var pop_flg = false;
	$('#hoge').popover({	
		trigger : 'click',
		html: true,
		animation:true,
	}).on('click', (e)=>{
		$('#hoge + div').css('text-align', 'center');
		$('.popover-content button').css('margin-bottom', '20px');
	});a
	$('#hoge').on('click', (e)=>{
		e.stopPropagation();
	});
	$('html').on('click', ()=>{
		$('#hoge').popover('hide');
	});

});
