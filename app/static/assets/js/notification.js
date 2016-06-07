/**
 * Created by imbernal on 6/1/16.
 */

swampdragon.open(function () {
	swampdragon.subscribe('notifications', 'notifications');
});

swampdragon.onChannelMessage(function (channels, message) {

	if (message.action === 'created') {
		addNotification(message.data);
	}
});


function addNotification(notification) {
    console.log(notification);
	$('#myModal').modal()
}
