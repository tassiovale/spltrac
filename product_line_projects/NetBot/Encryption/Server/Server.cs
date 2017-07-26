namespace Server
{
    class Server
    {
        private Stream getIncomingStream(NetworkStream clientStream)
        {
            return StreamEntschluesselung(clientStream);
        }

        private Stream getOutgoingStream(NetworkStream clientStream)
        {
            return StreamVerschluesselung(clientStream);
        }

        //Zwei Methoden um den gesamten NetworkStream des TCP Clients mit dem Rijndael Algorithmus zu ver-  und entschl�sseln
        private CryptoStream StreamVerschluesselung(NetworkStream clientStream)
        {
            // Erzeugen der Verschl�sselungsklasse
            RijndaelManaged RMCrypto = new RijndaelManaged();

            //Keys f�r die symmetrische Verschl�sselung
            byte[] Key = { 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16 };
            byte[] IV = { 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16 };

            //Erzeugen eines Verschl�sselten Datentroms, mit Hilfe der Keys und der Verschl�sselungsklasse
            return new CryptoStream(clientStream, RMCrypto.CreateEncryptor(Key, IV), CryptoStreamMode.Write);
        }

        private CryptoStream StreamEntschluesselung(NetworkStream clientStream)
        {
            // Erzeugen der Verschl�sselungsklasse
            RijndaelManaged RMCrypto = new RijndaelManaged();

            //Keys f�r die symmetrische Verschl�sselung
            byte[] Key = { 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16 };
            byte[] IV = { 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16 };

            //Erzeugen eines Entschl�sselten Datentroms, mit Hilfe der Keys und der Verschl�sselungsklasse
            return new CryptoStream(clientStream, RMCrypto.CreateDecryptor(Key, IV), CryptoStreamMode.Read);
        }
    }
}
