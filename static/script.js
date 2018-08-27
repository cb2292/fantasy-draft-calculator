// JavaScript Document

$(document).ready(function() {
	$(".hidden").hide();
	$(".faq_link").click(function() {
		if ($(this).parent().next().hasClass("hidden") === true)	{
			$(this).parent().next().show();
		}
		else	{
			return null;
		}
	});
});
