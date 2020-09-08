import random
msg = """Behind a big rock which looked down over the wide, straggling road that ran upward through the mountains crouched a long, lean figure. Snuggled against his right shoulder was a rifle, and the bearded face beneath the broad-brimmed panama was turned toward the roadway below. The hot sun beat down remorselessly, and its blinding rays were reflected from the rocks. Perspiration poured down the man’s face, and now and then he moved impatiently to brush away some buzzing insect. His head was raised slightly above the level of the rock, and from his point of vantage a splendid panorama spread out beneath him.

To his left lay the mountains, blue, remote, and full of rugged dignity all their own. To his right, a fertile South American valley revealed itself in the shimmering distance. Occasionally, as a light puff of wind came up from the lowlands, it brought with it the dull, heavy noise of an engine at work.

Half an hour passed, and then the first sign of life was revealed in the roadway below. There appeared round a bend a long line of mules, each of them burdened with two big packs. In front of the[6] train of mules walked a white man clad in dingy overalls.

The figure crouching behind the rock moved slightly and seemed to grow tense and expectant, while the eyes in the bearded face glinted as they peered down at the road.

Nothing happened, however. The mules plodded on, with their leader striding away ahead of them, and the lonely sentinel watched them until they had passed down the road and had vanished below the level of the rise which led them on to the plains.

“He ought to be coming soon now.”

The man spoke aloud, and there was a curious, metallic sound in his rasping voice.

Ten minutes passed, and then the clear, drumming sound of a horse’s hoofs came to him, and presently around the same jagged spur there appeared the figure of a man on horseback. He was riding along at a good pace, but the reins were lying loosely across the horse’s neck, and the animal was picking its way unguided down the rough surface of the road. Evidently it was on a familiar trail.

At the sight, the lurking figure grew tenser still, and the sound of a low growl, almost animal-like in character, might have been heard. Slowly the rifle was nestled closer to the shoulder. The panama hat, being too conspicuous, was pulled off and dropped behind him, after which the bare, rather bald head was lowered until the right cheek touched the stock of the gun. The left eye was closed, and the right[7] sighted along the barrel, which at the same time was shifted, following the man on horseback.

A few moments passed, during which the down-pointed muzzle shifted like a spy-glass, following the moving object. Then——

Crack! Into the still air a blue puff of smoke rose and hung for a moment above the rock. The drone of the bullet sounded clearly down the edge of the slope as the deadly missile hurled itself toward its mark. A quick cry came up from the roadway, and the weapon was stealthily withdrawn.

Quickly, however, the man behind the rock peered down, but when he did so he saw that blind chance had stepped in and thwarted him. The horse had apparently stumbled on a loose rock just as the shot was fired, and had reared back slightly to recover its footing; therefore, it was into the animal’s soft, rounded neck that the heavy bullet had bored its way, and not into the more precious target at which it had been aimed.

The creature was now lying in the roadway, and the convulsive movements of its limbs could be seen dimly through the little cloud of dust which had been raised by its fall.

The man on the horse’s back had been hurled in a heap by the side of the road, but as his would-be murderer watched, he saw him rise to his feet and stare up in the general direction of the rock from which the shot had been fired. Warned by that movement, the skulker swiftly jerked his head back and crouched still lower in his place.

[8]

“Curse him!” the hard voice grated. “He always has the fiend’s own luck!”

Grasping his rifle and hat, but still keeping on hands and knees, he began instinctively to crawl away under cover of the rock. He had gone no more than a yard, though, before he paused irresolutely and his fingers sought his belt.

There were other bullets in that belt, but the man’s failure had unnerved him, and a certain fatalistic instinct told him that he was not likely to succeed in a second attempt, now that the first had come to naught. The figure in the road would be on its guard now, and if another shot missed its mark, the point from which it had been fired would almost certainly be located. From that would only be a step to the discovery of the shooter’s identity, and the latter did not care to contemplate such a possibility. Consequently, with a snakelike movement, the lean figure resumed its progress away from the rocks, and presently, having reached the protection of large bowlders, straightened up a little more and increased its pace.

The fugitive knew that the man he had tried to kill was more than usually fond of the dying horse, and would probably delay at its side for a precious minute or two before attempting to solve the mystery of the shot. That delay promised to enable him to make good his escape, and he was resolved to take every possible advantage of it. For perhaps fifteen minutes he doubled and twisted, now ascending and now descending the foothills. At the end of that time he had reached the road again, and, watching[9] his chance, dodged across it. This latest move brought him into thick woods, through which he hurriedly threaded his way in the direction of the valley.

He hid his rifle in a hollow tree, and when he reached the little mining camp he had cunningly concealed all evidence of agitation or guilt.

The knowledge of the act was not destined to remain locked in his own breast, however, as he was soon to learn. At his destination, the Condor Mine, he found Charlie Floyd, the mine’s physician, waiting for him, and wearing a very stern expression.

“I have something important to say to you, Mr. Stone,” the young doctor said grimly, and led the way to a spot where they were out of earshot.

“What’s up?” demanded Stone, who was one of the two original owners of the mine. He and his partner, Winthrop Crawford, had only recently sold out for a cool million.

“Much,” was the grave answer. “I happened to be roaming about in the foothills back there a little while ago, and I saw you take that pot shot at Mr. Crawford.”

“What are you raving about?” growled Stone, with the greatest apparent surprise.

“I’m not raving at all, Mr. Stone. I always carry field glasses on my walks, as you know, and, being startled by the shot, I looked in that direction, saw the puff of smoke from behind the rock, and leveled my glasses on the spot. I saw you when you looked down to see if the bullet had done its work; saw you as plainly as if you had been not more than ten feet[10] away. There’s no possibility of a mistake. I was in a position to watch your movements afterward, and saw you sneaking away. I recognized your hat, too.”

Stone had wilted at first when the field glasses were mentioned, but now he seemed to have plucked up fresh courage, and even assumed a defiant attitude.

“Well, what are you going to do about it?” he demanded. “One or the other of us will have to kick the bucket sooner or later. Crawford has it in for me, and I only acted in self-defense. If I don’t get him first, he’ll get me as sure as fate.”

The young physician looked at him searchingly, but there was much more of pity than condemnation in his glance.

“You needn’t be afraid that I’m going to give you up to justice, Mr. Stone,” he said, after a pause. “You’ll resent it, of course, but I’m pretty sure that you’re not responsible for your actions. I hold your liberty, if not your life, in my hands, though, and I’m going to name a condition in return for my silence.”"""

# returns scrambled alphabet and I was too lazy to convert into array


def alphabet_randomizer():
    alphabet_str = "abcdefghijklmnopqrstuvwxyz"
    alphabet_list = []
    for letter in alphabet_str:
        alphabet_list.append(letter)
    random.shuffle(alphabet_list)
    return alphabet_list


# returns a scrambled message


def scrambler(msg):
    key_dict = {}
    coded_msg = ""
    original_alphabet = alphabet_randomizer()
    coded_alphabet = alphabet_randomizer()
    for i in range(len(original_alphabet)):
        key_dict[original_alphabet[i]] = coded_alphabet[i]
    for charater in msg:
        letter_use = False
        for key in key_dict:
            if charater == key:
                coded_msg += key_dict[key]
                letter_use = True
                break
        else:
            coded_msg += charater
    return coded_msg


print(scrambler(msg))
