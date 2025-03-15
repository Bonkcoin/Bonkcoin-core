<h1 align="center">
<img src="https://i.imgur.com/d9a8NfA.png" alt="Bonkcoin" width="300"/>
<br/><br/>
Bonkcoin Core [BONC, B]  
</h1>

言語を選択: [EN](./README.md) | [CN](./README_zh_CN.md) | [PT](./README_pt_BR.md) | [FA](./README_fa_IR.md) | [VI](./README_vi_VN.md) | [FR](./README_fr_FR.md) | JA | [DE](./README_de_DE.md)

Bonkcoinは、2013年のオリジナルのDogecoin shibesの1人によって作成されたコミュニティに焦点を当てた暗号通貨です。これは、オリジナルのDogecoinコミュニティと同じように、新しくて楽しいコミュニティを作成するために作成されました。

以前のすべてのバージョンとは異なり、Bonkcoinはレイヤー1のコインです。これは、排水する流動性プールがなく、ブラックリストに登録されたウォレットがなく、混乱するスマートコントラクトがないことを意味します。Bonkcoinはシンプルなブロックチェーンです。

Dogecoinと同様に、Bonkcoin Coreソフトウェアを使用すると、誰でもBonkcoinブロックチェーンネットワーク内でノードを操作でき、作業証明のためにScryptハッシュメソッドを使用します。これは、Dogecoin Core、Bitcoin Core、およびその他の暗号通貨から適応されています。

Bonkcoinネットワークで使用されるデフォルトの料金に関する情報については、[料金の推奨事項](doc/fee-recommendation.md)を参照してください。

**ウェブサイト:** [bonkscoin.io](https://bonkscoin.io)

## Dogecoinの違い

BonkcoinはDogecoinのフォークです。親しみやすさのために、BonkcoinをDogecoinに似せるように努めます。

変更点：

* アドレスは`D`ではなく`B`で始まります
* BIPS機能はブロック1000から開始されます
* AuxPowはブロック1500から開始されます（チェーンID：63）
* Bonkcoin用にテーマ設定されたGUI

## 使用法 💻

Bonkcoin Coreの旅を始めるには、[インストールガイド](INSTALL.md)と[入門](doc/getting-started.md)チュートリアルを参照してください。

Bonkcoin Coreが提供するJSON-RPC APIは自己文書化されており、`bonkcoin-cli help`を使用して参照できます。各コマンドの詳細情報は、`bonkcoin-cli help <command>`を使用して表示できます。あるいは、[Bitcoin Coreのドキュメント](https://developer.bitcoin.org/reference/rpc/)を参照してください。これは同様のプロトコルを実装しており、参照可能なバージョンを取得できます。

### ポート

Bonkcoin Coreはデフォルトでピアツーピア通信にポート`14327`を使用します。これは、「メインネット」ブロックチェーンを同期し、新しいトランザクションとブロックの情報を取得するために必要です。さらに、JSONRPCポートを開くことができ、デフォルトではメインネットノードのポート`15612`になります。RPCポートをパブリックインターネットに公開しないことを強くお勧めします。

| 機能     | メインネット | テストネット | regtest |
| :------- | ------: | ------: | ------: |
| P2P      |   14327 |   14328 |   14329 |
| RPC      |   15612 |   15613 |   15614 |

## 継続的な開発 💻

Bonkcoin Coreはオープンソースでコミュニティ主導のソフトウェアです。開発プロセスはオープンで公開されており、誰でもソフトウェアを見て、議論し、作業することができます。

主な開発リソース：

* [GitHubプロジェクト](https://github.com/Bonkcoin/Bonkcoin-core/projects)は、今後のリリースのために計画されている作業と進行中の作業を追跡するために使用されます。
* [GitHubディスカッション](https://github.com/Bonkcoin/Bonkcoin-core/discussions)は、Bonkcoin Coreソフトウェアの開発、基礎となるプロトコル、およびBONC資産に関連する計画されたおよび計画されていない機能について議論するために使用されます。


### バージョン戦略
バージョン番号は```major.minor.patch```のセマンティクスに従います。

### ブランチ
このリポジトリには3種類のブランチがあります：

- **master:** 安定版、最新の*major.minor*リリースの最新バージョンを含みます。
- **maintenance:** 安定版、以前のリリースの最新バージョンを含み、まだアクティブなメンテナンスが行われています。形式：```<version>-maint```
- **development:** 不安定版、計画されたリリースの新しいコードを含みます。形式：```<version>-dev```

*Masterおよびmaintenanceブランチはリリースによってのみ変更可能です。計画された*
*リリースには常に開発ブランチがあり、プルリクエストはそれらに対して送信する必要があります。メンテナンスブランチは**バグ修正のみ**のために存在します。新しい機能は、最も高いバージョンの開発ブランチに対して送信してください。*

## 貢献 🤝

このソフトウェアにバグを見つけたり、問題が発生した場合は、[問題システム](https://github.com/Bonkcoin/Bonkcoin-core/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5Bbug%5D+)を使用して報告してください。

Bonkcoin Coreの開発に参加する方法については、[貢献ガイド](CONTRIBUTING.md)を参照してください。多くの場合、[助けを求めるトピック](https://github.com/Bonkcoin/Bonkcoin-core/labels/help%20wanted)があり、あなたの貢献が大きな影響を与え、高く評価されます。

## コミュニティ 🐸

さまざまなソーシャルメディアでコミュニティに参加できます。
何が起こっているのかを確認し、人々と出会い、議論し、最新のミームを見つけ、Bonkcoinについて学び、助けを提供したり求めたり、プロジェクトを共有するために。

訪れるべき場所のいくつかを以下に示します：


* [Discord](https://discord.gg/rqtkgwsk6j)
* [Telegram](https://t.me/bonkscoin)
* [Twitter/X](https://x.com/bonkcoinpow)

## よくある質問 ❓

Bonkcoinに関する質問がありますか？答えはすでに[FAQ](doc/FAQ.md)またはディスカッションボードの[Q&Aセクション](https://github.com/Bonkcoin/Bonkcoin-core/discussions/categories/q-a)にあるかもしれません。

## ライセンス ⚖️
Bonkcoin CoreはMITライセンスの条件の下でリリースされています。詳細については[COPYING](COPYING)を参照するか、[opensource.org](https://opensource.org/licenses/MIT)を参照してください。
