from abc import abstractmethod, ABC
import pygame

class GUIElement(ABC):


    @abstractmethod
    def draw(self, screen):
        pass

    def is_hovered(self, m_pos):
        return (m_pos[0] > self.x and m_pos[0] < self.x + self.width) and (m_pos[1] > self.y and m_pos[1] < self.y + self.height)

    # make a text size lower and lower while we dont find a optimal size
    # --OPTIMIZE REQUIRED
    def get_optimal_size(self):
        low, high = 1, self.width
        best = 1

        while low <= high:
            mid = (low + high) // 2
            font = pygame.font.Font("engine/Settings/Fonts/Pixel.ttf", mid)
            if font.size(self.text)[0] <= self.width - 20:
                best = mid
                low = mid + 1
            else:
                high = mid - 1

        return best