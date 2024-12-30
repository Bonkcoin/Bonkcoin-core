<h1 align="center">
<img src="https://i.imgur.com/DDkfI9i.png" alt="Bonkcoin" width="300"/>
<br/><br/>
Bonkcoin Core [BONC, Ᵽ]
</h1>

Selecionar idioma: [EN](./README.md) | [CN](./README_zh_CN.md) | PT | [FA](./README_fa_IR.md) | [VI](./README_vi_VN.md) | [FR](./README_fr_FR.md) | [JA](./README_ja_JP.md) | [DE](./README_de_DE.md)

Bonkcoin é uma criptomoeda focada na comunidade, criada por um dos shibes originais do Dogecoin de 2013. Foi criada com um propósito, criar uma comunidade nova e divertida, assim como a comunidade original do Dogecoin.

Diferente de todas as iterações anteriores, o Bonkcoin é uma moeda de camada 1. Isso significa que não há piscinas de liquidez para drenar, carteiras em lista negra ou contratos inteligentes confusos. O Bonkcoin é uma blockchain simples.

Assim como o Dogecoin, o software Bonkcoin Core permite que qualquer pessoa opere um nó nas redes de blockchain do Bonkcoin e usa o método de hash Scrypt para o Proof of Work. Ele é adaptado do Bitcoin Core e de outras criptomoedas.

Para informações sobre as taxas padrão usadas na rede Bonkcoin, por favor consulte a [recomendação de taxas](doc/fee-recommendation.md).

**Website:** [bonkcoin.org](https://bonkcoin.org)

## Diferenças do Dogecoin

O Bonkcoin é um fork do Dogecoin. Para fins de familiaridade, tentaremos manter o Bonkcoin semelhante ao Dogecoin.

Mudanças:

* Endereços começam com `P` em vez de `D`
* Recursos BIPS começam no bloco gênese
* GUI temático para o Bonkcoin

## Uso 💻

Para iniciar sua jornada com o Bonkcoin Core, veja o [guia de instalação](INSTALL.md) e o tutorial [começando](doc/getting-started.md).

A API JSON-RPC fornecida pelo Bonkcoin Core é autoexplicativa e pode ser navegada com `bonkcoin-cli help`, enquanto informações detalhadas para cada comando podem ser visualizadas com `bonkcoin-cli help <comando>`. Alternativamente, veja a [documentação do Bitcoin Core](https://developer.bitcoin.org/reference/rpc/) - que implementa um protocolo semelhante - para obter uma versão navegável.

### Portas

O Bonkcoin Core, por padrão, usa a porta `14327` para comunicação peer-to-peer que é necessária para sincronizar a blockchain "mainnet" e se manter informado sobre novas transações e blocos. Adicionalmente, uma porta JSONRPC pode ser aberta, que por padrão é a porta `15612` para nós mainnet. É altamente recomendável não expor as portas RPC na internet pública.

| Função | mainnet | testnet | regtest |
| :------- | ------: | ------: | ------: |
| P2P      |   14327 |   44874 |   18444 |
| RPC      |   15612 |   44873 |   18332 |

## Desenvolvimento contínuo 💻

O Bonkcoin Core é um software de código aberto e orientado pela comunidade. O processo de desenvolvimento é aberto e publicamente visível; qualquer um pode ver, discutir e trabalhar no software.

Principais recursos de desenvolvimento:

* [Projetos do GitHub](https://github.com/bonkcoinppc/bonkcoin/projects) são usados para seguir o trabalho planejado e em progresso para futuros lançamentos.
* [Discussão do GitHub](https://github.com/bonkcoinppc/bonkcoin/discussions) é usada para discutir recursos, planejados e não planejados, relacionados tanto ao desenvolvimento do software Bonkcoin Core, quanto aos protocolos subjacentes e o ativo BONC.
* [Subreddit BonkcoinDev](https://www.reddit.com/r/bonkcoindev/)

### Estratégia de versão
Os números de versão seguem a semântica ```principal.menor.correção```.

### Branches
Existem 3 tipos de branches neste repositório:

- **master:** Estável, contém a versão mais recente do último lançamento *principal.menor*.
- **manutenção:** Estável, contém a versão mais recente de lançamentos anteriores, que ainda estão sob manutenção ativa. Formato: ```<versão>-manut```
- **desenvolvimento:** Instável, contém novo código para lançamentos planejados. Formato: ```<versão>-dev```

*Os branches master e de manutenção são exclusivamente mutáveis por lançamento. Lançamentos planejados sempre terão um branch de desenvolvimento e pull requests devem ser submetidos contra esses. Branches de manutenção são apenas para **correções de bugs,*** por favor, submeta novos recursos contra o branch de desenvolvimento com a versão mais alta.

## Contribuindo 🤝

Se você encontrar um bug ou tiver problemas com este software, por favor, relate usando o [sistema de problemas](https://github.com/bonkcoinppc/bonkcoin/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5Bbug%5D+).

Por favor, veja [o guia de contribuição](CONTRIBUTING.md) para saber como você pode participar do desenvolvimento do Bonkcoin Core. Muitas vezes há [tópicos buscando ajuda](https://github.com/bonkcoinppc/bonkcoin/labels/help%20wanted) onde suas contribuições terão alto impacto e serão muito apreciadas.

## Comunidades 🐸

Você pode se juntar às comunidades em diferentes mídias sociais.
Para ver o que está acontecendo, conhecer pessoas e discutir, encontrar o último meme, aprender sobre o Bonkcoin, dar ou pedir ajuda, para compartilhar seu projeto.

Aqui estão alguns lugares para visitar:

* [r/Bonkcoin](https://www.reddit.com/r/bonkcoin/)
* [Discord](https://bonkcoin.org/discord)
* [Telegram](https://t.me/BonkcoinGroup)
* [Twitter/X](https://twitter.com/BonkcoinNetwork)

## Perguntas Frequentes ❓

Você tem uma pergunta sobre o Bonkcoin? A resposta pode estar na [FAQ](doc/FAQ.md) ou na [seção de Perguntas e Respostas](https://github.com/bonkcoinppc/bonkcoin/discussions/categories/q-a) do quadro de discussão!

## Licença ⚖️
O Bonkcoin Core é lançado sob os termos da licença MIT. Veja
[COPYING](COPYING) para mais informações ou veja
[opensource.org](https://opensource.org/licenses/MIT)