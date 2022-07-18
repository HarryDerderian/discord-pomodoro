import random
from re import A

HANGMAN = ['''
  +---+
  |
  |
  |
======''', 
'''
  +---+
  |   O
  |
  |
======''', 
'''
  +---+
  |   O
  |   |
  |
======''', 
'''
  +---+
  |   O
  |  /|
  |
======''', 
'''
  +---+
  |   O
  |  /|\ 
  |
======''', 
'''
  +---+
  |   O
  |  /|\ 
  |  /
======''',
'''
  +---+
  |   O
  |  /|\ 
  |  / \ 
======
 GAME OVER'''
]

words = [
['absolute'], ['abstract'], ['academic'], ['accepted'], 
['accident'], ['accuracy'], ['accurate'], ['achieved'], 
['acquired'], ['activity'], ['actually'], ['addition'], 
['adequate'], ['adjacent'], ['adjusted'], ['advanced'], 
['advisory'], ['advocate'], ['affected'], ['aircraft'], 
['alliance'], ['although'], ['aluminum'], ['analysis'], 
['announce'], ['anything'], ['anywhere'], ['apparent'], 
['appendix'], ['approach'], ['approval'], ['argument'], 
['artistic'], ['assembly'], ['assuming'], ['athletic'], 
['attached'], ['attitude'], ['attorney'], ['audience'], 
['autonomy'], ['aviation'], ['bachelor'], ['bacteria'], 
['baseball'], ['bathroom'], ['becoming'], ['benjamin'], 
['birthday'], ['boundary'], ['breaking'], ['breeding'], 
['building'], ['bulletin'], ['business'], ['calendar'], 
['campaign'], ['capacity'], ['casualty'], ['catching'], 
['category'], ['Catholic'], ['cautious'], ['cellular'], 
['ceremony'], ['chairman'], ['champion'], ['chemical'], 
['children'], ['circular'], ['civilian'], ['clearing'], 
['clinical'], ['clothing'], ['collapse'], ['colonial'], 
['colorful'], ['commence'], ['commerce'], ['complain'], 
['complete'], ['composed'], ['compound'], ['comprise'], 
['computer'], ['conclude'], ['concrete'], ['conflict'], 
['confused'], ['congress'], ['consider'], ['constant'], 
['consumer'], ['continue'], ['contract'], ['contrary'], 
['contrast'], ['convince'], ['corridor'], ['coverage'], 
['covering'], ['creation'], ['creative'], ['criminal'], 
['critical'], ['crossing'], ['cultural'], ['currency'], 
['customer'], ['database'], ['daughter'], ['daylight'], 
['deadline'], ['deciding'], ['decision'], ['decrease'], 
['deferred'], ['definite'], ['delicate'], ['delivery'], 
['describe'], ['designer'], ['detailed'], ['diabetes'], 
['dialogue'], ['diameter'], ['directly'], ['director'], 
['disabled'], ['disaster'], ['disclose'], ['discount'], 
['discover'], ['disorder'], ['disposal'], ['distance'], 
['distinct'], ['district'], ['dividend'], ['division'], 
['doctrine'], ['document'], ['domestic'], ['dominant'], 
['dominate'], ['doubtful'], ['dramatic'], ['dressing'], 
['dropping'], ['duration'], ['dynamics'], ['earnings'], 
['economic'], ['educated'], ['efficacy'], ['eighteen'], 
['election'], ['electric'], ['eligible'], ['emerging'], 
['emphasis'], ['employee'], ['endeavor'], ['engaging'], 
['engineer'], ['enormous'], ['entirely'], ['entrance'], 
['envelope'], ['equality'], ['equation'], ['estimate'], 
['evaluate'], ['eventual'], ['everyday'], ['everyone'], 
['evidence'], ['exchange'], ['exciting'], ['exercise'], 
['explicit'], ['exposure'], ['extended'], ['external'], 
['facility'], ['familiar'], ['featured'], ['feedback'], 
['festival'], ['finished'], ['firewall'], ['flagship'], 
['flexible'], ['floating'], ['football'], ['foothill'], 
['forecast'], ['foremost'], ['formerly'], ['fourteen'], 
['fraction'], ['franklin'], ['frequent'], ['friendly'], 
['frontier'], ['function'], ['generate'], ['generous'], 
['genomics'], ['goodwill'], ['governor'], ['graduate'], 
['graphics'], ['grateful'], ['guardian'], ['guidance'], 
['handling'], ['hardware'], ['heritage'], ['highland'], 
['historic'], ['homeless'], ['homepage'], ['hospital'], 
['humanity'], ['identify'], ['identity'], ['ideology'], 
['imperial'], ['incident'], ['included'], ['increase'], 
['indicate'], ['indirect'], ['industry'], ['informal'], 
['informed'], ['inherent'], ['initiate'], ['innocent'], 
['inspired'], ['instance'], ['integral'], ['intended'], 
['interact'], ['interest'], ['interior'], ['internal'], 
['interval'], ['intimate'], ['intranet'], ['invasion'], 
['involved'], ['isolated'], ['judgment'], ['judicial'], 
['junction'], ['keyboard'], ['landlord'], ['language'], 
['laughter'], ['learning'], ['leverage'], ['lifetime'], 
['lighting'], ['likewise'], ['limiting'], ['literary'], 
['location'], ['magazine'], ['magnetic'], ['maintain'], 
['majority'], ['marginal'], ['marriage'], ['material'], 
['maturity'], ['maximize'], ['meantime'], ['measured'], 
['medicine'], ['medieval'], ['memorial'], ['merchant'], 
['midnight'], ['military'], ['minimize'], ['minister'], 
['ministry'], ['minority'], ['mobility'], ['modeling'], 
['moderate'], ['momentum'], ['monetary'], ['moreover'], 
['mortgage'], ['mountain'], ['mounting'], ['movement'], 
['multiple'], ['national'], ['negative'], ['nineteen'], 
['northern'], ['notebook'], ['numerous'], ['observer'], 
['occasion'], ['offering'], ['official'], ['offshore'], 
['operator'], ['opponent'], ['opposite'], ['optimism'], 
['optional'], ['ordinary'], ['organize'], ['original'], 
['overcome'], ['overhead'], ['overseas'], ['overview'], 
['painting'], ['parallel'], ['parental'], ['patented'], 
['patience'], ['peaceful'], ['periodic'], ['personal'], 
['persuade'], ['petition'], ['physical'], ['pipeline'], 
['platform'], ['pleasant'], ['pleasure'], ['politics'], 
['portable'], ['portrait'], ['position'], ['positive'], 
['possible'], ['powerful'], ['practice'], ['precious'], 
['pregnant'], ['presence'], ['preserve'], ['pressing'], 
['pressure'], ['previous'], ['princess'], ['printing'], 
['priority'], ['probable'], ['probably'], ['producer'], 
['profound'], ['progress'], ['property'], ['proposal'], 
['prospect'], ['protocol'], ['provided'], ['provider'], 
['province'], ['publicly'], ['purchase'], ['pursuant'], 
['quantity'], ['question'], ['rational'], ['reaction'], 
['received'], ['receiver'], ['recovery'], ['regional'], 
['register'], ['relation'], ['relative'], ['relevant'], 
['reliable'], ['reliance'], ['religion'], ['remember'], 
['renowned'], ['repeated'], ['reporter'], ['republic'], 
['required'], ['research'], ['reserved'], ['resident'], 
['resigned'], ['resource'], ['response'], ['restrict'], 
['revision'], ['rigorous'], ['romantic'], ['sampling'], 
['scenario'], ['schedule'], ['scrutiny'], ['seasonal'], 
['secondly'], ['security'], ['sensible'], ['sentence'], 
['separate'], ['sequence'], ['sergeant'], ['shipping'], 
['shortage'], ['shoulder'], ['simplify'], ['situated'], 
['slightly'], ['software'], ['solution'], ['somebody'], 
['somewhat'], ['southern'], ['speaking'], ['specific'], 
['spectrum'], ['sporting'], ['standard'], ['standing'], 
['standout'], ['sterling'], ['straight'], ['strategy'], 
['strength'], ['striking'], ['struggle'], ['stunning'], 
['suburban'], ['suitable'], ['superior'], ['supposed'], 
['surgical'], ['surprise'], ['survival'], ['sweeping'], 
['swimming'], ['symbolic'], ['sympathy'], ['syndrome'], 
['tactical'], ['tailored'], ['takeover'], ['tangible'], 
['taxation'], ['taxpayer'], ['teaching'], ['tendency'], 
['terminal'], ['terrible'], ['thinking'], ['thirteen'], 
['thorough'], ['thousand'], ['together'], ['tomorrow'], 
['touching'], ['tracking'], ['training'], ['transfer'], 
['traveled'], ['treasury'], ['triangle'], ['tropical'], 
['turnover'], ['ultimate'], ['umbrella'], ['universe'], 
['unlawful'], ['unlikely'], ['valuable'], ['variable'], 
['vertical'], ['victoria'], ['violence'], ['volatile'], 
['warranty'], ['weakness'], ['weighted'], ['whatever'], 
['whenever'], ['wherever'], ['wildlife'], ['wireless'], 
['withdraw'], ['woodland'], ['workshop'], ['yourself']]

def getWord(wordList): #returns word randomly selected from list
    wordIndex = random.randint(0, len(words) -1 )
    return wordList[wordIndex]

def displayGame(missedLetters, correctLetters, secretWord):
    print(HANGMAN[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    print()

    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)): 
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def main():
    print('H A N G M A N')
    missedLetters = ''
    correctLetters = ''
    secretWord = getWord(words)
    secretWord = ' '.join(secretWord)
    gameIsDone = False

    while True:
        displayGame(missedLetters, correctLetters, secretWord)

        guess = getGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters = correctLetters + guess

            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes! The secret word is "' + secretWord +
                    '"! You have won!')
                gameIsDone = True
        else:
            missedLetters = missedLetters + guess

            if len(missedLetters) == len(HANGMAN) - 1:
                displayGame(missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!\nAfter ' +
                    str(len(missedLetters)) + ' missed guesses and ' +
                    str(len(correctLetters)) + 
                    ' correct guesses, the word was "'
                     + secretWord + '"')
                gameIsDone = True

        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getWord(words)
                secretWord = ' '.join(secretWord)
            else:
                break

main()
