<<<<<<< HEAD
(function($){ // block scope
	jQuery.fn.log = function (msg) {
		if (!window.console || !console) return;
		if (window.console || console.firebug){
			msg = msg || '';
			if(msg !== '') msg += ': ';
			console.log("%s%o", msg, this);
		}
		return this;
	};
	$.extend({
		log : function (msg) {
			if (!window.console || !console) return;
			if (window.console || console.firebug) {
				console.log("%s", msg);
			}
		}
	});
=======
(function($){ // block scope
	jQuery.fn.log = function (msg) {
		if (!window.console || !console) return;
		if (window.console || console.firebug){
			msg = msg || '';
			if(msg !== '') msg += ': ';
			console.log("%s%o", msg, this);
		}
		return this;
	};
	$.extend({
		log : function (msg) {
			if (!window.console || !console) return;
			if (window.console || console.firebug) {
				console.log("%s", msg);
			}
		}
	});
>>>>>>> cf450579b98693d8f8b89011abc39ce3e39311b6
})(jQuery);