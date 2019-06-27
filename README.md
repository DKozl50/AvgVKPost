# AvgVKPost
vk_api code to make an average vk post

Makes average text by either composing it letter-by-letter or via word-by-word and average picture composing it with average pixels such that

i-th letter/word/pixel is the most common i-th letter/word/pixel in every other text/photo

Here are some results for search query "#выпускной" (' symbols are markers for start and end of texts)

Letter-by-letter: '#выпускной                                                                                                                    о                                                                                       и                                      о                           '

Letter-by-letter excluding spaces: '#выпускнойопиоаосоноооааооооооаооооасоооаоооооеааооиоааоооооаоаооооооооаоооиооооооооооооаоеоооаооооааоооиеиоооаоааооооеоакоиоеоооооаонаооооаиоеооаооооооаиеноеааоеораеоааооооооооеиоооаоооооаооооеоеоеооеоасоооиеовоеаиооооаееосаоооаоооосоаеоиааоаоосаеоиоеоотаоиораанноооетоеоеоиоеааои'

Word-by-word: '#выпускной #выпускной выпускной в в и ксш. в #выпускной #выпускной #выпускной #выпускной #выпускной и и #выпускной #выпускной в и #выпускной и и и и и и и и в и и в душе в и'

Word-by-word excluding "и", "в", "на": '#выпускной #выпускной выпускной в в и ксш. в #выпускной #выпускной #выпускной #выпускной #выпускной и и #выпускной #выпускной в и #выпускной и и и и и и и и в и и в душе в и'

Pixel-by-pixel average picture(965x966): ![Average picture](https://i.imgur.com/84e4Tba.jpg)
