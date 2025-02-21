<h1 align="center">
<img src="https://i.imgur.com/d9a8NfA.png" alt="Bonkcoin" width="300"/>
<br/><br/>
Bonkcoin Core [BONC, B]  
</h1>


Sprache ändern: [EN](./README.md) | [CN](./README_zh_CN.md) | [PT](./README_pt_BR.md) | [FA](./README_fa_IR.md) | [VI](./README_vi_VN.md) | [FR](./README_fr_FR.md) | [JA](./README_ja_JP.md) | DE | 



Bonkcoin, erstellt von einem der ursprünglichen Dogecoin-Shibes, ist eine Community-fokussierte Kryptowährung, mit dem Ziel, eine neue und spaßige Community, ähnlich der ursprünglichen Dogecoin-Community, zu schaffen.

Im Gegensatz zu allen vorherigen Iterationen ist Bonkcoin ein Layer-1 Coin. 
Das bedeutet, es gibt keine Liquiditätspools, keine Sperrung von Wallets und keine verwirrenden Smart Contracts. 
Bonkcoin ist eine einfache, eigenständige Blockchain.

Die Bonkcoin Core-Software ermöglicht es jedem, einen Node in den Bonkcoin-Blockchain-Netzwerken zu betreiben und verwendet die Scrypt-Hashing-Methode für den "Proof of Work". 
Sie wurde aus den Programmen Dogecoin Core, Bitcoin Core und anderen Kryptowährungen angepasst.

Für Informationen zu den Standardgebühren im Bonkcoin-Netzwerk lesen Sie die [Gebührenempfehlungen](doc/fee-recommendation_DE.md).

**Website:** [bonkscoin.io](https://bonkscoin.io)

## Unterschiede zu Dogecoin

Bonkcoin ist eine Abspaltung von Dogecoin. Um die Vertrautheit zu wahren, werden wir versuchen, Bonkcoin ähnlich wie Dogecoin zu behandeln.

Änderungen:

* Adressen beginnen mit `B` statt `D`
* BIPS-Funktionen übernommen
* AuxPow Chain ID 63 (Merged Mining aktiviert)
* UI im Bonc-Style



## Verwendung 💻

Um Ihre Reise mit Bonkcoin Core zu beginnen, lesen Sie den [Quick Guide](doc/README_windows_DE.md), [Installationsanweisungen](INSTALL.md) und das [Einrichtungstutorial](doc/getting-started.md).

Die JSON-RPC-API von Bonkcoin Core ist selbstdokumentierend und kann mit bonkcoin-cli help durchsucht werden, während detaillierte Informationen zu jedem Befehl mit bonkcoin-cli help <Befehl> angezeigt werden können. 
Alternativ lesen Sie die [Bitcoin Core Dokumentation](https://developer.bitcoin.org/reference/rpc/) - die ein ähnliches Protokoll implementiert - um eine durchsuchbare Version zu erhalten.

### Ports

Bonkcoin Core verwendet standardmäßig den Port `14327` für die Peer-to-Peer-Kommunikation, 
die zum Synchronisieren der "mainnet"-Blockchain und zum Informieren über neue Transaktionen und Blöcke benötigt wird. 
Zusätzlich kann ein JSONRPC-Port geöffnet werden, der standardmäßig für Mainnet-Knoten auf Port `15612` eingestellt ist. 
Es wird dringend empfohlen, RPC-Ports nicht dem öffentlichen Internet preiszugeben.

| Function | mainnet | testnet | regtest |
| :------- | ------: | ------: | ------: |
| P2P      |   14327 |   44874 |   18444 |
| RPC      |   15612 |   44873 |   18332 |

## Fortlaufende Entwicklung 💻

Bonkcoin Core ist eine Open-Source- und Community-getriebene Software. 
Der Entwicklungsprozess ist offen und öffentlich einsehbar; jeder kann die Software sehen, darüber diskutieren und daran arbeiten.


Hauptentwicklungsressourcen:

* [GitHub Projekte](https://github.com/Bonkcoin/Bonkcoin-core/projects) werden verwendet,
 um geplante und laufende Arbeiten für bevorstehende Veröffentlichungen zu verfolgen.

* [GitHub Discussion](https://github.com/Bonkcoin/Bonkcoin-core/discussions) wird genutzt, 
  um Features (geplante und ungeplante) zu diskutieren die mit der Entwicklung der Bonkcoin Core-Software, den zugrunde liegenden Protokollen und dem BONC-Vermögenswert zusammenhängen.




### Versionsstrategie

Versionsnummern folgen dem Schema ```major.minor.patch```.

### Branches

Es gibt 3 Arten von Branches in diesem Repository:

- **master**: Stabil, enthält die neueste Version der letzten *major.minor* Veröffentlichung.
- **maintenance**: Stabil, enthält die neueste Version früherer Veröffentlichungen, die noch aktiv gewartet werden. Format: <version>-maint
- **development**: Instabil, enthält neuen Code für geplante Veröffentlichungen. Format: ```<version>-dev```

*Master- und Wartungs-Branches sind ausschließlich durch Veröffentlichungen änderbar.*
*Geplante Veröffentlichungen haben immer einen Entwicklungs-Branch, und Pull Requests sollten gegen diese eingereicht werden.*
*Wartungs-Branches sind **nur für Bugfixes gedacht,** reichen Sie bitte neue Funktionen gegen den Entwicklungszweig mit der höchsten Version ein.*

## Mitwirken 🤝

Wenn Sie einen Fehler finden oder Probleme mit dieser Software haben, melden Sie dies bitte über das [Report System](https://github.com/Bonkcoin/Bonkcoin-core/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5Bbug%5D+).

Bitte sehen Sie sich den [Beitrag zur Mitwirkung](CONTRIBUTING.md) an, um zu erfahren, wie Sie an der Entwicklung von Bonkcoin Core teilnehmen können. 
Oft gibt es [Themen, bei denen Hilfe benötigt wird](https://github.com/Bonkcoin/Bonkcoin-core/labels/help%20wanted), bei denen Ihre Beiträge einen großen Einfluss haben und sehr geschätzt werden.

## Communities 🐸

Sie können sich der Community in verschiedenen sozialen Medien anschließen, um Leute zu treffen, zu diskutieren, 
die neuesten Bonc-Memes zu finden, etwas über Bonkcoin zu lernen oder um Ideen zu teilen.

Hier sind einige Links:

* [Discord](https://discord.gg/rqtkgwsk6j) Offizieller Bonkcoin Discord Server
* [Telegram](https://t.me/bonkscoin)
* [Twitter/X](https://x.com/bonkcoinpow)

## Häufig gestellte Fragen ❓

Haben Sie eine Frage zu Bonkcoin? 
Eine Antwort befindet sich vielleicht bereits im [FAQ](doc/FAQ_DE.md) oder im [Frage-und-Antwort-Bereich](https://github.com/Bonkcoin/Bonkcoin-core/discussions/categories/q-a) des Diskussionsforums!

## Lizenz ⚖️
Bonkcoin Core wird unter den Bedingungen der MIT-Lizenz veröffentlicht. Siehe 
[COPYING](COPYING) für weitere Informationen oder besuchen Sie
[opensource.org](https://opensource.org/licenses/MIT)
