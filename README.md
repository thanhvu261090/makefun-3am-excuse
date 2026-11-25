# The 3 AM Excuse

[![make.fun bounty](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/thanhvu261090/makefun-3am-excuse/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/thanhvu261090/makefun-3am-excuse/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

Entry for the [make.fun bounty "The 3 AM Excuse"](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878) — a single line under 200 characters, in the voice of a hardware wallet that will not sign a transaction at 3 AM. A judge model compares lines two at a time, weighing being on subject first, then originality, the wallet's voice, how well the line uses the hour, then economy.

## The entry

> 3 AM? My private keys are asleep, my screen's on night mode, and 'just one quick sign' is how wallets get drained — try me at sunrise.

## How it works

`main.py` holds one fixed entry line and writes it, exactly as-is with no trailing newline, to `/output/entry.txt`. Before writing, `gate_check` enforces the competition gate: the text must be 1–199 UTF-8 characters, a single line with no leading or trailing whitespace. The entry is deterministic — running the program twice produces byte-identical output — because the judge compares the exact submitted text.

Run it with:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
