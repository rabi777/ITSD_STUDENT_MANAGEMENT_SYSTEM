$(document).on("change keyup", "#amount", function(){
	var fee = $('#fee').val();
	var amt = $('#amount').val();
	var paid = $('#paid').val($('#amount').val());
	var dis = 0;

	if (paid!='' && amt!=0){
		paid = parseFloat($('amount').val())
		var dis = (((parseFloat(fee) - parseFloat(paid)) * 100) / fee);
		$('$lack').val(parseFloat(amt) - parseFloat(paid));
	}

	if (amt == '' && paid==''){
		$('#paid').val()
		$('#discount').val()
	}

	if (parseFloat(amt) > parseFloat(fee)){
		$('#discount').css("color", 'red');
	}
	else{
		$('#discount').css({"color" : "black"})
	}
	$('#discount').val(parseFloat(dis))
});


$(document).on("change keyup", "#discount", function(){
	var fee = paseFloat($('#fee').val());
	var dis = 0;
	dis = ((fee * parseFloat($(this).val()))) / 100;
	var amt = fee - dis;

	$('#paid').val(parseFloat(amt))
	$('#amount').val(parseFloat(amt))
});

$(document).on("change keyup", '#paid', function(){
	b = $('#amount').val();
	var pay = $('#paid').val();
	if(pay==''){
		$('#lack').val(0)
	}
	if(pay!=''){
		paid = parseFloat($('#paid').val());
	}
	if(pay!='' && b!=''){
		var lack = parseFloat(b) - parseFloat(paid)
		$('#lack').val(parseInt(lack))
	}
	if($('#lack').val() = 0){
		$('#lack').css('color' : 'red');
	}
	else{
		$('#lack').css('color', 'black');
	}
});

$(document).on("change keyup", "#pay", function(){
	 b = $('#b').val()
	 var pay=$('#pay').val()
	 if(pay==''){
	 	$('#lack').val(0)
	 }
	 if(pay!=''){
	 	paid = parseFloat($('#pay').val());
	 }
	 if(pay!='' && b!=''){
	 	var lack = parseFloat(b) - parseFloat(paid)
	 	$('#lack').val(parseFloat(lack));
	 }
	 if($('#lack').val()<0){
	 	$('#lack').css('color', 'red')
	 }else{
	 	$('#lack').css('color', 'black');
	 }
});
