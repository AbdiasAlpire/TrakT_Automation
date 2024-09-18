from behave import *

from features.pages.DashboardPage import DashboardPage
from features.pages.HistoryPage import HistoryPage
from features.pages.MovieDetailPage import MovieDetailPage
from features.pages.MoviesPage import MoviesPage

movies_url = "https://trakt.tv/movies/trending"

@given("I am in the Movies page")
def step_impl(context):
    dashboard_page = DashboardPage(context.driver)
    context.dashboard_page = dashboard_page
    dashboard_page.click_movies_link()
    #movie_url_got = dashboard_page.am_i_in_dashboard()
    #assert movie_url_got, movies_url


@when("I click a movie")
def step_impl(context):
    movies_page = MoviesPage(context.driver)
    context.movies_page = movies_page
    movies_page.click_a_movie()
    movie_detail_page = MovieDetailPage(context.driver)
    context.movie_detail_page = movie_detail_page
    context.current_movie_title = movie_detail_page.get_movie_title()

@step("I click Add to History button")
def step_impl(context):
    movie_details_page = MovieDetailPage(context.driver)
    context.movie_details_page = movie_details_page
    movie_details_page.click_add_to_history_button()


@step("I click profile dropdown")
def step_impl(context):
    movie_details_page = MovieDetailPage(context.driver)
    context.movie_details_page = movie_details_page
    movie_details_page.hover_user_dropdown_button()


@step("I click History button")
def step_impl(context):
    movie_details_page = MovieDetailPage(context.driver)
    context.movie_details_page = movie_details_page
    movie_details_page.click_history_button()



@then("I should be able to see my added movie")
def step_impl(context):
    history_page = HistoryPage(context.driver)
    context.history_page = history_page
    movie_text_on_detail_page = context.current_movie_title
    movie_text_on_history = context.history_page.get_movie_title_in_history()
    assert movie_text_on_history, movie_text_on_detail_page



@then("I should not be able to see my removed movie")
def step_impl(context):
    history_page = HistoryPage(context.driver)
    context.history_page = history_page
    movie_text_is_found = history_page.get_movie_title_in_history(context.current_movie_title)
    assert movie_text_is_found, False
