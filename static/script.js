// JavaScript Document

$(document).ready(function() {
	$(".ishidden").hide();
	$(".faq_link").click(function() {
		if ($(this).parent().next().hasClass("ishidden") === true)	{
			$(this).parent().next().show();
		}
		else	{
			return null;
		}
	});
});
