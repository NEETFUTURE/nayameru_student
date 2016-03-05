+$(function() {
	'use strict';

	let input_arr = ["search-box", "book1", "book2", "book3"];
	var clearAllInput = () =>{
		let i = 0;
		$.each(input_arr, ()=>{
			$("#" + input_arr[i]).val("");
			i++;
		});
	};
	$('#hoge').popover({	
		trigger : 'click',
		html: true,
		animation:true,
	}).on('click', (e)=>{
		$('#hoge + div').css('text-align', 'center');
		$('.popover-content button').css('margin-bottom', '20px');
	});

	$('#login,#content').on('click', ()=>{
		if($('#fuga')){
			$('#hoge').popover('hide');
		}
	});
	$(document).on('click', '#fuga', (e)=> {
		if($('#fuga')){
			$('#hoge').popover('hide');
		}
	});
	$('#add').on('click',()=>{
		let str = $('#book1').val()+','+$('#book2').val()+','+$('#book3').val();
		clearAllInput();
		$('#search-box').val(str);
		$('#add-modal').modal('hide');
	});
});
