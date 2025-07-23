# map_tool_fullsize.py
from PIL import Image
import json, os
from collections import deque

def split_mask_fullsize(mask_path, output_dir, alpha_threshold=128):
    """
    Разбивает RGBA-маску на отдельные fullsize RGBA-маски.
    В каждой маске остаётся только один домик (островок непрозрачных пикселей);
    фон — полностью прозрачный.
    """
    os.makedirs(output_dir, exist_ok=True)

    # Загружаем RGBA-маску
    img = Image.open(mask_path).convert("RGBA")
    w, h = img.size
    alpha = img.split()[3]       # альфа-канал
    pix = alpha.load()

    visited = [[False]*h for _ in range(w)]
    result = {}

    def bfs(sx, sy, idx):
        queue = deque([(sx, sy)])
        coords = []
        visited[sx][sy] = True

        # Собираем все пиксели этой компоненты
        while queue:
            x, y = queue.popleft()
            coords.append((x, y))
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x+dx, y+dy
                if 0 <= nx < w and 0 <= ny < h and not visited[nx][ny]:
                    if pix[nx, ny] > alpha_threshold:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

        # Создаём fullsize RGBA-картинку, фон — прозрачный
        mask_rgba = Image.new("RGBA", (w, h), (255, 255, 255, 0))
        m_pix = mask_rgba.load()
        for x, y in coords:
            # белый цвет, полностью непрозрачный
            m_pix[x, y] = (255, 255, 255, 255)

        fname = f"map_mask_house_{idx}.png"
        path = os.path.join(output_dir, fname)
        mask_rgba.save(path)
        return path

    idx = 1
    for x in range(w):
        for y in range(h):
            if not visited[x][y] and pix[x, y] > alpha_threshold:
                result[f"house_{idx}"] = bfs(x, y, idx)
                idx += 1

    # Сохраняем JSON‑индекс
    cfg_path = os.path.join(output_dir, "map_mask_index.json")
    with open(cfg_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    return result

if __name__ == "__main__":
    masks = split_mask_fullsize("map_mask.png", "masks", alpha_threshold=128)
    print("Generated fullsize RGBA masks:", masks)
    input("Нажмите Enter чтобы выйти…")