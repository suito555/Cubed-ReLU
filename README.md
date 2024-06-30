# Cubed ReLU
新しく作った活性化関数のCubed ReLUです。関数の値は以下の通りです。<br>
<br>
**Cubed ReLU(x) = max(0,x)^3 / 3**<br>
<br>
この関数は、<br>
・ReLU特有のスパース性を得たい<br>
・微分の際に綺麗な値になれば収束が早いのではないか<br>
といった考えで作っています。<br>
<br>
以下、元々個人で見るために作ったものなので雑な検証です。日本語のwikipediaのデータセット(3GB程)を用いて以下のような結果になっています。<br>

![relu_pattern_full](https://github.com/suito555/Cubed-ReLU/blob/main/assets/relu_pattern_full.png)

![relu_pattern_partial](https://github.com/suito555/Cubed-ReLU/blob/main/assets/relu_pattern_partial.png)

![relu_1_3vs1_6_full](https://github.com/suito555/Cubed-ReLU/blob/main/assets/relu_1_3vs1_6_full.png)

![relu_pattern_partial](https://github.com/suito555/Cubed-ReLU/blob/main/assets/relu_pattern_partial.png)

**20000stepsの時の値**

| ReLU | Train Loss | Val Loss |
|---|---|---|
| x | 2.8380 | 2.7170 |
|  |  |  |
| x^2 | 2.7958 | 2.6758 |
| x^2 / 2 | 2.7930 | 2.6742 |
|  |  |  |
| x^3 | 2.7946 | 2.6722 |
| x^3 / 2 | 2.7914 | 2.6737 |
| x^3 / 3 | 2.7874 | 2.6692 |
| x^3 / 4.5 | 2.7886 | 2.6690 |
| x^3 / 6 | 2.7895 | 2.6675 |
| x^3 / 9 | 2.7919 | 2.6710 |
|  |  |  |
| x^4 / 4 | 2.7993 | 2.6787 |


**x^3 1/3 と x^3 1/6**
| Step | 1/3 Train Loss | 1/6 Train Loss | 1/3 Val Loss | 1/6 Val Loss |
|---|---|---|---|---|
| 10000 | 2.8908 | 2.8911 | 2.8195 | 2.8202 |
| 20000 | 2.7890 | 2.7920 | 2.6707 | 2.6690 |
| 30000 | 2.7688 | 2.7725 | 2.6295 | 2.6341 |
| 40000 | 2.7596 | 2.7626 | 2.6640 | 2.6667 |
| 50000 | 2.7312 | 2.7323 | 2.6086 | 2.6082 |


全体的な結果の値としては1/3〜1/6辺りが良さそうに思えたので、微分の値を考慮して1/3としています。<br>

### 補足
この検証の不足な点として<br>
・データセットのサイズがやや小さい<br>
・他の乱数ではどうなのかが不明<br>
・開始時wandbでエラーが発生する状況であったため、一部のデータのtrainのlogが荒い<br>
・当初の目的であるスパース性は一体どうなったのか<br>
など、多くの改善点があります。個人でなら雑に検証をするぐらいで良いだろうと思っていたのが原因です。しかし、今から全てを再検証するのは時間的に大変なものがある事と、上手く行った以上は公開しないのも違うと思い公開しました。しっかりと検証してみたい方は活性化関数を変えるだけの簡単な実装ですので試してみてください。<br>
<br>
後にwandbを再インストールしたらバグが治ったので、Cubed Relu(x^3 1/3)が学習可能であることを一応示しておきます。<br>
![WB_ReLU](https://github.com/suito555/Cubed-ReLU/blob/main/assets/W%26B%20Chart%20x%5E3%20%201_3.png)
<br>
参考文献<br>
Squared ReLU https://arxiv.org/abs/2109.08668<br>
StarReLU https://arxiv.org/abs/2210.13452<br>
dReLU https://arxiv.org/abs/2406.05955<br>
<br>
GPT2 parameters 35.66M<br>
n_layer=8<br>
n_head=8<br>
n_embd=512<br>
eval_iters=2000<br>
block_size=1024<br>
batch_size=2<br>
eval_interval=2000<br>
warmup_iters=100<br>
dropout=0.1<br>
learning_rate=3e-4<br>
min_lr=3e-5<br>
gradient_accumulation_steps=32<br>
torch.compile=True<br>
