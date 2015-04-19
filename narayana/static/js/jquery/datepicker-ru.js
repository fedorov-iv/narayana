jQuery(function($){
	$.datepicker.regional['ru'] = {
		closeText: '�������',
		prevText: '����',
		nextText: '����',
		currentText: '������',
		monthNames: ['������','�������','����','������','���','����',
		'����','������','��������','�������','������','�������'],
		monthNamesShort: ['���','���','����','���','���','����',
		'����','���','����','���','���','���'],
		dayNames: ['�����������','�����������','�������','�����','�������','�������','�������'],
		dayNamesShort: ['���','��','��','��','��','���','���'],
		dayNamesMin: ['���','��','��','��','��','���','���'],
		weekHeader: 'Нед',
		dateFormat: 'dd.mm.yy',
		firstDay: 1,
		isRTL: false,
		showMonthAfterYear: false,
		yearSuffix: ''};
	$.datepicker.setDefaults($.datepicker.regional['ru']);
});


