# Museum of the Year 3000

[![make.fun](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb/badge)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb)

Entry for the [Museum of the Year 3000](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb) bounty on make.fun.

## The label

> Group chat, c. 2025. Dozens of humans shouted into one small glowing rectangle at once, then apologized for replying late to the people sitting beside them.

## How it works

`main.py` is deterministic, standard-library-only Python. It writes the single
museum label (156 characters, one line, English) to `/output/entry.txt`, where
the sealed scorer checks it and the judge compares it two at a time against
the other entries.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
