# Build notes

## Competition

The Meeting That Should Have Been an Email
(`u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9`).
Gate: `/output/entry.txt` must be UTF-8 text of 1 to 200 characters,
not only white space. The kit supplied no starter template (only
`RULES.txt`, `competition.yaml`, the CLI, and harness files), so the
repository starts with a draft commit and every entry file below
was authored in this session. The GitHub repository is created
later by the coordinator; no remote was added here.

## Judge brief, in criterion order

1. One line, plainly a joke, unmistakably about a meeting that
   should have been an email; anything else loses to any
   on-subject joke.
2. The laugh lands on its own with no setup, the turn arriving
   by the last word, and a reader who has sat in that meeting
   laughs.
3. Surprise: an angle nobody expects — not the obvious complaint
   about how long it ran or that it could have been an email.
4. Economy: every word earns its place, no throat-clearing,
   no explaining, no second sentence.
5. Recognition: names something true about meetings people have
   actually sat through, so the laugh comes with a nod.

A line needing insider or team knowledge is weaker than one
that stands alone. Length for its own sake does not count.
The twist belongs in the last word or words, and the cap is a
ceiling, not a target.

## Variants drafted

All variants below are original lines written for this
competition; none reuses a line from another competition, and
none reproduces a house text.

1. "Everyone had already read the email; we met to pretend we
   hadn't." — first draft. Strong pretence angle, but 65
   characters, two clauses, and the twist is spread over the
   last three words.
2. "We spent the meeting writing the email that should have
   replaced it." — rejected: circular idea, ends on the weak
   word "it", and explains itself.
3. "The meeting's only decision was to send the email we'd all
   already read." — rejected: setup-heavy, clunky, the laugh
   arrives late and flat.
4. "Forty-five minutes, nine people, one email, read aloud —
   slowly." — rejected: a complaint about how long the meeting
   ran, which criterion 3 warns against, and a fragment rather
   than a plain joke.
5. "We met to discuss the email, then emailed about the
   meeting." — rejected: the loop is cute but muddles the
   subject; the email-about-a-meeting turn drifts away from
   the meeting that should have been an email.

## Polishes of the winner (each re-run and verified byte-for-byte)

- Draft: "Everyone had already read the email; we met to pretend
  we hadn't." (65 characters)
- Polish 1: new angle — the email was never read at all.
  "Nine of us met to discuss an email nobody had opened."
  (53 characters) Shorter, one sentence, twist in the last word.
- Polish 2: "opened" became "read" (opening an email is not
  reading it; the failure that matters is the reading), and
  "an email" became "the email" (the specific email the meeting
  was called about). "Nine of us met to discuss the email
  nobody had read." (52 characters)
- Polish 3: tested cutting "had" — "nobody read" (49
  characters) — and rejected it: "read" without "had" is
  ambiguous on a first read, while "had read" pins the past
  tense at once. Also tested "none of us had read" (echoes
  "Nine of us", weaker) and "debate" for "discuss" ("discuss"
  is the true meeting verb). Final line unchanged from
  polish 2. (52 characters)

## Verification

The program was run repeatedly, including at the default
`/output/entry.txt` path and via an `OUTPUT_PATH` override.
Every run produced byte-identical output: 52 characters,
52 bytes, no trailing newline, SHA-256
`b7026001de428adf4757b1c5a83df42c9f5d162c0ec77f438e95a5119d857ab5`.

## Files

- `main.py` — entrypoint; writes the entry verbatim.
- `README.md` — description and run instructions, with the
  competition's three live make.fun badge lines at the top.
- `BUILD.md` — this file.
- `LICENSE` — MIT.
- `.gitignore` — keeps local output out of the repo.
- `.makefun/owner.json` — payout wallet.
