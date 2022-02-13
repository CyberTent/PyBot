from lib import *

errortxt = ('Команда должна выглядить следующим образом:\n`.boom <столбцы> <строки> <бомбы>`\n\n',
            'Можно не указывать строки, столбцы и бомбы, но тогда я построю своё поле.')
errortxt = ''.join(errortxt)


class Minesweeper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def boom(self, ctx, columns=None, rows=None, bombs=None):
        if columns is None or rows is None and bombs is None:
            if columns is not None or rows is not None or bombs is not None:
                await ctx.send(errortxt)
                return
            else:
                # Рандомит строки и столбцы от 4 до 13, ели их не задал юзер
                # Бомбы рандомятся по этой формуле ((columns * rows) - 1) / 2.5
                columns = random.randint(2, 9)
                rows = random.randint(2, 9)
                bombs = columns * rows - 1
                bombs = bombs / 2.5
                bombs = round(random.randint(5, round(bombs)))
        try:
            columns = int(columns)
            rows = int(rows)
            bombs = int(bombs)
        except ValueError:
            await ctx.send(errortxt)
            return
        if columns > 9 or rows > 9:
            await ctx.send('Больше 9 строк и столбцов выбрать нельзя. Все претензии к дискорду, не ко мне...')
            return
        if columns < 1 or rows < 1 or bombs < 1:
            await ctx.send('Я.ТЕБЯ.ПОНЯЛ...играть ты не будешь')
            return
        if bombs + 1 > columns * rows:
            await ctx.send(':boom:**БУМ**, слишком много бомб, даже пустого места не осталось...')
            return

        # Создание сетки из нулей (списко внутри списка)
        grid = [[0 for num in range(columns)] for num in range(rows)]

        # Цикл для заполнения сетки бомбами
        loop_count = 0
        while loop_count < bombs:
            x = random.randint(0, columns - 1)
            y = random.randint(0, rows - 1)
            if grid[y][x] == 0:
                grid[y][x] = 'B'
                loop_count = loop_count + 1
            if grid[y][x] == 'B':
                pass

        # Проходим через каждую точку на сетке, чтоб дать им "правильные" номера
        pos_x = 0
        pos_y = 0
        while pos_x * pos_y < columns * rows and pos_y < rows:
            adj_sum = 0
            # Проверяет соседние точки у проверяемой точки
            for (adj_y, adj_x) in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
                # Для избежания ошибок с индексами лучше заюзать try except (слався костыль)
                try:
                    if grid[adj_y + pos_y][adj_x + pos_x] == 'B' and adj_y + pos_y > -1 and adj_x + pos_x > -1:
                        # увеличивает цифру на сетке в зависимости от количества бомб вокруг
                        adj_sum = adj_sum + 1
                except Exception:
                    pass
            if grid[pos_y][pos_x] != 'B':
                grid[pos_y][pos_x] = adj_sum
            if pos_x == columns - 1:
                pos_x = 0
                pos_y = pos_y + 1
            else:
                pos_x = pos_x + 1

        string_builder = []
        for the_rows in grid:
            string_builder.append(''.join(map(str, the_rows)))
        string_builder = '\n'.join(string_builder)
        # замена цифер и B на нужные эмодзи и закрывает их в спойлеры
        string_builder = string_builder.replace('0', '||:zero:||')
        string_builder = string_builder.replace('1', '||:one:||')
        string_builder = string_builder.replace('2', '||:two:||')
        string_builder = string_builder.replace('3', '||:three:||')
        string_builder = string_builder.replace('4', '||:four:||')
        string_builder = string_builder.replace('5', '||:five:||')
        string_builder = string_builder.replace('6', '||:six:||')
        string_builder = string_builder.replace('7', '||:seven:||')
        string_builder = string_builder.replace('8', '||:eight:||')
        final = string_builder.replace('B', '||:bomb:||')

        percentage = columns * rows
        percentage = bombs / percentage
        percentage = 100 * percentage
        percentage = round(percentage, 2)

        await ctx.send(content=f'\U0000FEFF\n{final}')  # , embed=embed)

    @boom.error
    async def minesweeper_error(self, ctx, error):
        await ctx.send(errortxt)
        return


def setup(bot):
    print('minesweeper loaded')
    bot.add_cog(Minesweeper(bot))