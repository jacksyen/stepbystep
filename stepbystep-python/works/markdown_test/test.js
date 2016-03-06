/**
 * Created by patrick on 15/12/17.
 */
(function() {
	var data = null,
		DB_NAME = 'tests' + document.URL;

	var drawButton = function(elParent, index) {
		var el = new Element('div', {
			'class': 'result'
		});

		var title = (data[index] || 'Untested');

		var elStatus = new Element('div', {
			'class': 'status ' + (isSuccess(title) ? 'success' : '') + (isFail(title) ? 'fail' : ''),
			'html': ''
		});

		el.adopt(elStatus);

		el.adopt(new Element('button', {
			'data-index': index,
			'type': 'button',
			'text': 'Success',
			'events': {
				'click': function() {
					data[index] = 'Success';
					localStorage.setItem(DB_NAME, JSON.stringify(data));
					//elStatus.set('html', 'Status: ' + data[index]);
					if (isSuccess(data[index])) elStatus.addClass('success');
					else elStatus.removeClass('success');
					if (isFail(data[index])) elStatus.addClass('fail');
					else elStatus.removeClass('fail');
				}
			}
		}));

		el.adopt(new Element('button', {
			'data-index': index,
			'type': 'button',
			'text': 'Fail',
			'events': {
				'click': function() {
					data[index] = 'Fail';
					localStorage.setItem(DB_NAME, JSON.stringify(data));
					//elStatus.set('html', 'Status: ' + data[index]);
					if (isSuccess(data[index])) elStatus.addClass('success');
					else elStatus.removeClass('success');
					if (isFail(data[index])) elStatus.addClass('fail');
					else elStatus.removeClass('fail');
				}
			}
		}));

		elParent.grab(el);
	};

	var isSuccess = function(text) {
		return text === 'Success';
	};

	var isFail = function(text) {
		return text === 'Fail';
	};

	window.onload = function() {
		if (!window.localStorage) {
			alert('No localStorage');
			return;
		}

		try {
			data = JSON.parse(localStorage.getItem(DB_NAME));
			if (!data) {
				data = {};
			}
		} catch (e) {
			data = {};
		}

		var els = $(document).getElements('li');
		els.each(drawButton);
	};
})();
