from django.contrib import admin

from .models import Curation, Season, Color


@admin.register(Curation)
class CurationAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "season_list",
        "color_list",
        "product_list",
        "created_at",
        "like_count",
    )
    list_filter = ("seasons", "colors")
    search_fields = ("title", "description")
    filter_horizontal = ("seasons", "colors", "products")

    def season_list(self, obj):
        return ", ".join([season.name for season in obj.seasons.all()])

    def color_list(self, obj):
        return ", ".join([color.name for color in obj.colors.all()])

    def product_list(self, obj):
        return ", ".join([product.name for product in obj.products.all()])

    def like_count(self, obj):
        return obj.likes.count()

    season_list.short_description = "계절"
    color_list.short_description = "색상"
    like_count.short_description = "좋아요 수"


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    pass


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass
