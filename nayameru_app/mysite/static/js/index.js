+$(function() {
	'use strict';

	var pop_flg = false;
	var hidePop = () =>{
		$('#hoge').popover('hide');
	};
	$('#hoge').popover({	
		trigger : 'click',
		html: true,
		animation:true,
	}).on('click', (e)=>{
		$('#hoge + div').css('text-align', 'center');
		$('.popover-content button').css('margin-bottom', '20px');
		pop_flg = true;
	});

	$('#login,#content').on('click', ()=>{
		if(pop_flg){
			$('#hoge').popover('hide').trigger('click');
			pop_flg = false;
		};
	});
	$(document).on('click', '#fuga', ()=> {
		$('#hoge').popover('hide').trigger('click');
		pop_flg = false;
	});
});
