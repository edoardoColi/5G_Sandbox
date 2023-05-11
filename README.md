# 5G Sandbox

## Table of Contents
1. [Overview of 5G](#overview-of-5g)
2. [Overview of 802,11](#overview-of-802,11)
3. [Comparison of 5G and 802,11](#comparison-of-5g-and-802,11)
4. [Traffic MAC Analyzer](#traffic-mac-analyzer)
	- [Execution](#execution)

## Overview of 5G
-Per poter aggiungere un nuovo gruppo \<NEW_GROUP\> possiamo utilizzare il comando `groupadd <NEW_GROUP>`. In questo modo verrà aggiunta la voce \<NEW_GROUP\> ai file `/etc/group` e `/etc/gshadow`, nel caso un gruppo con lo stesso nome sia già presente verrà stampato un messaggio di errore.  
Per cancellare un gruppo \<OLD_GROUP\> possiamo utilizzare il comando `groupdel <OLD_GROUP>`. In questo modo verrà rimossa la voce \<OLD_GROUP\> ai file `/etc/group` e `/etc/gshadow`, nel caso un gruppo con lo stesso nome non sia presente verrà stampato un messaggio di errore.  
Per verificare la stato dei gruppi degli utenti si può utilizzare `groups`. Per maggiori dettagli consultare il manuale.  
- Utenti  
Per aggiungere un Utente utilizziamo `adduser username`  
in questo modo verrà creata la directory del nuovo utente(/home/username) e inizializzata come `/etc/skel`.  
Successivamente dovrà essere impostata una password utente tramite `passwd username`.  
Per rimuovere un Utente utilizziamo `userdel username` e nel caso volessimo cancellare anche la directory dell'utente  `userdel -r username`  
la rimozione dell'utente comprende anche la rimozione da tutti i gruppi in cui l'utente era membro.  
  
Possiamo aggiungere i nuovi utenti ai gruppi, per farlo utilizziamo  
`usermod -aG wheel username`  
Possiamo ache rimuovere un utente da un gruppo con `gpasswd -d username wheel`  
All'interno dei comandi utilizziamo il gruppo `wheel` che corrisponde al gruppo di utenti che può utilizzare il comando sudo, come specificato nel file `/etc/sudoers`.  

## Overview of 802.11
Per poter aggiungere un nuovo gruppo \<NEW_GROUP\> possiamo utilizzare il comando `groupadd <NEW_GROUP>`. In questo modo verrà aggiunta la voce \<NEW_GROUP\> ai file `/etc/group` e `/etc/gshadow`, nel caso un gruppo con lo stesso nome sia già presente verrà stampato un messaggio di errore.  
Per cancellare un gruppo \<OLD_GROUP\> possiamo utilizzare il comando `groupdel <OLD_GROUP>`. In questo modo verrà rimossa la voce \<OLD_GROUP\> ai file `/etc/group` e `/etc/gshadow`, nel caso un gruppo con lo stesso nome non sia presente verrà stampato un messaggio di errore.  
Per verificare la stato dei gruppi degli utenti si può utilizzare `groups`. Per maggiori dettagli consultare il manuale.  
- Utenti  
Per aggiungere un Utente utilizziamo `adduser username`  
in questo modo verrà creata la directory del nuovo utente(/home/username) e inizializzata come `/etc/skel`.  
Successivamente dovrà essere impostata una password utente tramite `passwd username`.  
Per rimuovere un Utente utilizziamo `userdel username` e nel caso volessimo cancellare anche la directory dell'utente  `userdel -r username`  
la rimozione dell'utente comprende anche la rimozione da tutti i gruppi in cui l'utente era membro.  
  
Possiamo aggiungere i nuovi utenti ai gruppi, per farlo utilizziamo  
`usermod -aG wheel username`  
Possiamo ache rimuovere un utente da un gruppo con `gpasswd -d username wheel`  
All'interno dei comandi utilizziamo il gruppo `wheel` che corrisponde al gruppo di utenti che può utilizzare il comando sudo, come specificato nel file `/etc/sudoers`.  


## Comparison of 5G and 802.11
Per poter aggiungere un nuovo gruppo \<NEW_GROUP\> possiamo utilizzare il comando `groupadd <NEW_GROUP>`. In questo modo verrà aggiunta la voce \<NEW_GROUP\> ai file `/etc/group` e `/etc/gshadow`, nel caso un gruppo con lo stesso nome sia già presente verrà stampato un messaggio di errore.  
Per cancellare un gruppo \<OLD_GROUP\> possiamo utilizzare il comando `groupdel <OLD_GROUP>`. In questo modo verrà rimossa la voce \<OLD_GROUP\> ai file `/etc/group` e `/etc/gshadow`, nel caso un gruppo con lo stesso nome non sia presente verrà stampato un messaggio di errore.  
Per verificare la stato dei gruppi degli utenti si può utilizzare `groups`. Per maggiori dettagli consultare il manuale.  
- Utenti  
Per aggiungere un Utente utilizziamo `adduser username`  
in questo modo verrà creata la directory del nuovo utente(/home/username) e inizializzata come `/etc/skel`.  
Successivamente dovrà essere impostata una password utente tramite `passwd username`.  
Per rimuovere un Utente utilizziamo `userdel username` e nel caso volessimo cancellare anche la directory dell'utente  `userdel -r username`  
la rimozione dell'utente comprende anche la rimozione da tutti i gruppi in cui l'utente era membro.  
  
Possiamo aggiungere i nuovi utenti ai gruppi, per farlo utilizziamo  
`usermod -aG wheel username`  
Possiamo ache rimuovere un utente da un gruppo con `gpasswd -d username wheel`  
All'interno dei comandi utilizziamo il gruppo `wheel` che corrisponde al gruppo di utenti che può utilizzare il comando sudo, come specificato nel file `/etc/sudoers`.  

## Traffic MAC Analyzer
Per poter aggiungere un nuovo gruppo \<NEW_GROUP\> possiamo utilizzare il comando `groupadd <NEW_GROUP>`. In questo modo verrà aggiunta la voce \<NEW_GROUP\> ai file `/etc/group` e `/etc/gshadow`, nel caso un gruppo con lo stesso nome sia già presente verrà stampato un messaggio di errore.  
Per cancellare un gruppo \<OLD_GROUP\> possiamo utilizzare il comando `groupdel <OLD_GROUP>`. In questo modo verrà rimossa la voce \<OLD_GROUP\> ai file `/etc/group` e `/etc/gshadow`, nel caso un gruppo con lo stesso nome non sia presente verrà stampato un messaggio di errore.  
Per verificare la stato dei gruppi degli utenti si può utilizzare `groups`. Per maggiori dettagli consultare il manuale.  
- Utenti  
Per aggiungere un Utente utilizziamo `adduser username`  
in questo modo verrà creata la directory del nuovo utente(/home/username) e inizializzata come `/etc/skel`.  
Successivamente dovrà essere impostata una password utente tramite `passwd username`.  
Per rimuovere un Utente utilizziamo `userdel username` e nel caso volessimo cancellare anche la directory dell'utente  `userdel -r username`  
la rimozione dell'utente comprende anche la rimozione da tutti i gruppi in cui l'utente era membro.  
  
Possiamo aggiungere i nuovi utenti ai gruppi, per farlo utilizziamo  
`usermod -aG wheel username`  
Possiamo ache rimuovere un utente da un gruppo con `gpasswd -d username wheel`  
All'interno dei comandi utilizziamo il gruppo `wheel` che corrisponde al gruppo di utenti che può utilizzare il comando sudo, come specificato nel file `/etc/sudoers`.  

### Execution
```
./MACshuffle.sh -h
```








------------------------------------------------------------------------------
cos'e 5g
perche si puo' fare una sandbox
cose 802.11
cosa si vuole fare con lo script
come funziona lo script
gestione del caso live stream


Il supporto per gli indirizzi MAC randomizzati non  sempre disponibile su tutti i dispositivi Android a causa di limitazioni hardware o software. In alcuni casi, i dispositivi pi vecchi potrebbero non essere in grado di supportare la funzionalit di indirizzi MAC randomizzati a causa delle limitazioni hardware, ad esempio di una scheda di rete che non dispone di hardware per la generazione di indirizzi MAC randomizzati. Inoltre, l'implementazione degli indirizzi MAC randomizzati potrebbe essere influenzata anche dalle politiche di privacy e sicurezza del produttore del dispositivo o dell'operatore di rete mobile. Alcuni produttori potrebbero decidere di non implementare questa funzionalit perch non rientra nei loro obiettivi di sicurezza e privacy, oppure perch la loro politica di sicurezza prevede l'utilizzo di indirizzi MAC statici per motivi di tracciabilit e identificazione dei dispositivi.


WPA3 (Wi-Fi Protected Access 3)  stata introdotta per migliorare la sicurezza delle reti Wi-Fi rispetto alla precedente versione di sicurezza WPA2. Tra le principali ragioni per cui  stato introdotto WPA3 ci sono:
 1 Maggiore resistenza agli attacchi di tipo brute-force: WPA3 utilizza un sistema di autenticazione pi robusto rispetto a WPA2, basato sull'algoritmo di autenticazione Dragonfly. Questo rende pi difficile per gli attaccanti individuare le password delle reti Wi-Fi.
 2 Miglioramenti alla privacy: WPA3 introduce un nuovo protocollo di crittografia di tipo forward secrecy, che migliora la privacy degli utenti. Questo significa che anche se un attaccante riesce a decrittare il traffico di una sessione di rete Wi-Fi, non sar in grado di decrittare il traffico delle sessioni precedenti o successive.
 3 Protezione dalle vulnerabilit legate alla gestione delle chiavi di sicurezza: WPA3 migliora la gestione delle chiavi di sicurezza rispetto a WPA2, introducendo il protocollo di scambio di chiavi Simultaneous Authentication of Equals (SAE). SAE fornisce una maggiore protezione contro gli attacchi di tipo dictionary e permette di impostare password pi robuste.
Inoltre, negli ultimi anni si  assistito all'adozione di indirizzi MAC randomizzati per aumentare la privacy degli utenti. L'indirizzo MAC (Media Access Control)  un identificatore univoco assegnato a ogni dispositivo che si connette a una rete Wi-Fi e pu essere utilizzato per tracciare l'attivit degli utenti.
Gli indirizzi MAC randomizzati sono stati introdotti per proteggere la privacy degli utenti impedendo il tracciamento della loro attivit online. In pratica, il dispositivo utilizza un indirizzo MAC diverso ad ogni connessione, rendendo pi difficile per le societ di analisi o gli attaccanti tracciare l'attivit degli utenti. Tuttavia, l'utilizzo di indirizzi MAC randomizzati potrebbe causare problemi di compatibilit con alcune reti Wi-Fi, poich alcuni dispositivi richiedono un indirizzo MAC univoco per la connessione alla rete.


5G Sandbox
Per quanto riguarda il settore della comunicazione mobile, il 5G rappresenta una svolta tecnologica, poich permette di supportare nuovi servizi e applicazioni come la realt aumentata, la realt virtuale, il cloud computing, l'Internet delle Cose (IoT) e molto altro ancora. Inoltre, il 5G supporta un maggior numero di dispositivi per unit di superficie rispetto al 4G, consentendo di soddisfare la crescente domanda di connettivit mobile. Il 5G utilizza una combinazione di diverse tecnologie, come la modulazione OFDM (Orthogonal Frequency Division Multiplexing) e l'accesso radio NB-IoT (Narrowband Internet of Things), per fornire una maggiore capacit di trasmissione dati, una velocit di trasferimento pi elevata e una latenza pi bassa rispetto al 4G.

Per quanto riguarda il WiFi, il 5G e il WiFi sono tecnologie complementari che possono lavorare insieme per offrire una connessione pi veloce e affidabile. Il WiFi  una tecnologia di rete locale wireless che utilizza le onde radio per connettere dispositivi ad una rete. Il 5G, d'altra parte,  una tecnologia di rete cellulare che offre una connessione mobile veloce e affidabile. Il protocollo 802.11 del WiFi e il protocollo 5G sono stati sviluppati per funzionare in modo indipendente, ma possono essere utilizzati insieme per offrire una connessione Internet pi veloce e affidabile. Ad esempio, alcune implementazioni di 5G, come il 5G FWA (Fixed Wireless Access), utilizzano il WiFi come mezzo per trasmettere i dati in un'area specifica.
------------------------------------------------------------------------------1
5G is the fifth generation of wireless technology that promises to deliver faster data transfer speeds, lower latency, and increased network capacity. It is designed to enable a wide range of new applications and use cases that were previously not possible with 4G technology, such as remote surgery, autonomous vehicles, and smart cities.

5G technology is based on a new radio access technology called New Radio (NR), which uses higher frequency bands (millimeter waves) than previous generations of wireless technology. This allows 5G networks to deliver much faster data transfer speeds compared to 4G.

In addition to faster speeds, 5G also promises to reduce latency (the time it takes for a device to communicate with the network) to under 1 millisecond, which is critical for real-time applications such as gaming, virtual reality, and remote surgery.

5G networks also offer greater network capacity, which means they can support more devices and data traffic than 4G networks. This is important for the growth of the Internet of Things (IoT) and other connected devices, which require reliable and high-speed network connections.

Overall, 5G is expected to revolutionize the way we use wireless technology and enable new applications that were previously not possible. However, the rollout of 5G networks is still ongoing and faces challenges such as the need for more infrastructure and the use of higher frequency bands that have limited coverage compared to lower frequency bands.
------------------------------------------------------------------------------2
802.11 is a set of standards for wireless local area networks (WLANs) developed by the Institute of Electrical and Electronics Engineers (IEEE). It is commonly known as Wi-Fi, and it allows devices to connect to the internet or other devices wirelessly. The 802.11 standards define the protocols and technologies for wireless communication, including the frequency bands used for transmission, the data transfer rates, and the security and encryption methods used to protect the data being transmitted. There are several different versions of the 802.11 standard, including 802.11a, 802.11b, 802.11g, 802.11n, and 802.11ac, each with different specifications and capabilities. 802.11 has become an essential part of modern networking, enabling wireless connectivity in homes, offices, and public spaces.
------------------------------------------------------------------------------3
5G and 802.11 are both wireless communication technologies, but they differ in several key areas. Here's a comparison of 5G and 802.11 in terms of their similarities and differences, use cases and applications, advantages and disadvantages, and future developments.

    Similarities and differences between 5G and 802.11:

Both 5G and 802.11 are wireless communication technologies that use radio waves to transmit data. However, they differ in their frequency bands, coverage areas, and data rates. 5G operates in higher frequency bands, providing faster data speeds but requiring more infrastructure to provide coverage. 802.11 operates in lower frequency bands and is primarily used for local area networking.

    Comparison of 5G and 802.11 use cases and applications:

5G is primarily used for mobile communications, including smartphones, IoT devices, and autonomous vehicles. It can also be used for industrial automation, virtual and augmented reality, and other applications that require high-speed, low-latency data transfer. 802.11 is primarily used for local area networking, such as in homes, offices, and public spaces. It can also be used for IoT applications and other low-bandwidth use cases.

    Comparison of 5G and 802.11 advantages and disadvantages:

5G offers faster data transfer rates, lower latency, and greater capacity than 802.11. However, it requires more infrastructure and is more expensive to deploy. 802.11 is more widely available and less expensive to deploy, but it has lower data transfer rates and higher latency.

    Future of 5G and 802.11 in relation to each other:

5G and 802.11 will continue to coexist, with 5G providing high-speed, low-latency mobile communications and 802.11 providing local area networking. However, there may be opportunities for convergence between the two technologies, such as using 5G to provide high-speed backhaul for 802.11 networks.

Overall, both 5G and 802.11 have their strengths and weaknesses, and their use cases and applications will continue to evolve as new technologies and devices emerge.
---------------------------------------------------------------------------4
Lo standard 802 si riferisce a una serie di standard di comunicazione sviluppati dallo Institute of Electrical and Electronics Engineers (IEEE) per reti locali e wireless.

Il più noto è lo standard 802.11, che è il protocollo di base per la tecnologia Wi-Fi utilizzata per la connessione a Internet senza fili. Questo standard definisce le specifiche per la trasmissione dati attraverso le onde radio, inclusi la frequenza, la velocità di trasmissione e la sicurezza dei dati.

Ci sono anche altri standard 802 che definiscono le specifiche per reti locali cablate (ad esempio 802.3 Ethernet), reti wireless di area personale (ad esempio 802.15 Bluetooth) e reti wireless di area metropolitana (ad esempio 802.16 WiMAX).

In generale, gli standard 802 consentono l'interoperabilità tra dispositivi di diversi produttori e forniscono una guida per l'implementazione delle reti in modo che funzionino in modo affidabile e sicuro.