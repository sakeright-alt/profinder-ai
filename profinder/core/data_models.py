from dataclasses import dataclass
from typing import Optional


@dataclass
class Influencer:
    id: int
    name: str
    platform: str
    followers: int
    avg_likes: float
    avg_comments: float
    avg_story_views: float
    avg_reach: float
    category: Optional[str] = None

    @property
    def engagement_rate(self) -> float:
        if self.followers <= 0:
            return 0.0
        return (self.avg_likes + self.avg_comments) / self.followers
