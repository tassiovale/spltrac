package feature.history;

import application.common.Message;
import application.common.TextMessage;

public class HistoryAspect {

	/*public static void setHistoryFileForServer(String[] args) {
		HistoryImpl.instance.setFile(new File("server.log"));
	}
	
	public static void setHistoryFileForClient(String[] args) {
		HistoryImpl.instance.setFile(new File("client_" + args[3] + ".log"));
	}
	
	public void serverBroadcast(TextMessage msg) {
		HistoryImpl.instance.logTextMessage(msg);
	}
	
	public void clientMessageReceived(Message msg) {
		if (msg instanceof TextMessage) {
			HistoryImpl.instance.logTextMessage((TextMessage) msg);
		}
	}*/
	
}
