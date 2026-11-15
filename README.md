# Tuxhe Engineer · practice

Unsolved exercises from the [Tuxhe Engineer](https://www.youtube.com/@tuxhe.engineer) Shorts. Each folder matches one
video: watch it, then make the tests pass.

Ejercicios sin resolver de los Shorts de Tuxhe Engineer: mira el vídeo y haz que pasen los tests.

| Video | Topic | Folder |
|---|---|---|
| V001a | Comprehensions in Python: the three parts and their cases | [`python/V001a-comprehension-parts`](python/V001a-comprehension-parts) |

## Setup

Needs [uv](https://docs.astral.sh/uv/) and [just](https://just.systems/).

```bash
uv sync                               # Python 3.12+ and the dev tools
just test V001a-comprehension-parts   # run one exercise's tests
just check                            # lint, types, and that every test loads
```

Every test fails until you solve it. Solutions are not published.

## License

[MIT](LICENSE)
