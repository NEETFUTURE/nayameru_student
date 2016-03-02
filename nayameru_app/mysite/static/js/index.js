+$(function() {
	'use strict';
	$('#hoge').popover({
		trigger : 'click',
		html: true,
	});
	$('#hoge').on('click', ()=>{
		$('#hoge + div').css('text-align', 'center');
		$('.popover-content button').css('margin-bottom', '20px');
	});
	$('.content').on('click', ()=>{
		$('#hoge').popover('hide');
	})
});
