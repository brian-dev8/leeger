from leeger.calculator.all_time_calculator import AWALAllTimeCalculator
from leeger.calculator.all_time_calculator.GameOutcomeAllTimeCalculator import \
    GameOutcomeAllTimeCalculator
from leeger.calculator.all_time_calculator.PlusMinusAllTimeCalculator import PlusMinusAllTimeCalculator
from leeger.calculator.all_time_calculator.PointsScoredAllTimeCalculator import \
    PointsScoredAllTimeCalculator
from leeger.calculator.all_time_calculator.SSLAllTimeCalculator import SSLAllTimeCalculator
from leeger.calculator.all_time_calculator.ScoringShareAllTimeCalculator import \
    ScoringShareAllTimeCalculator
from leeger.calculator.all_time_calculator.ScoringStandardDeviationAllTimeCalculator import \
    ScoringStandardDeviationAllTimeCalculator
from leeger.calculator.all_time_calculator.SingleScoreAllTimeCalculator import \
    SingleScoreAllTimeCalculator
from leeger.calculator.all_time_calculator.SmartWinsAllTimeCalculator import SmartWinsAllTimeCalculator
from leeger.calculator.year_calculator import \
    ScoringStandardDeviationYearCalculator
from leeger.calculator.year_calculator import SingleScoreYearCalculator
from leeger.calculator.year_calculator.AWALYearCalculator import AWALYearCalculator
from leeger.calculator.year_calculator.GameOutcomeYearCalculator import GameOutcomeYearCalculator
from leeger.calculator.year_calculator.PlusMinusYearCalculator import PlusMinusYearCalculator
from leeger.calculator.year_calculator.PointsScoredYearCalculator import PointsScoredYearCalculator
from leeger.calculator.year_calculator.SSLYearCalculator import SSLYearCalculator
from leeger.calculator.year_calculator.ScoringShareYearCalculator import ScoringShareYearCalculator
from leeger.calculator.year_calculator.SmartWinsYearCalculator import SmartWinsYearCalculator
from leeger.model.league import League, Year
from leeger.model.stat.AllTimeStatSheet import AllTimeStatSheet
from leeger.model.stat.YearStatSheet import YearStatSheet


def leagueStatSheet(league: League, **kwargs) -> AllTimeStatSheet:
    # Game Outcome
    wins = GameOutcomeAllTimeCalculator.getWins(league, **kwargs)
    losses = GameOutcomeAllTimeCalculator.getLosses(league, **kwargs)
    ties = GameOutcomeAllTimeCalculator.getTies(league, **kwargs)
    winPercentage = GameOutcomeAllTimeCalculator.getWinPercentage(league, **kwargs)
    wal = GameOutcomeAllTimeCalculator.getWAL(league, **kwargs)
    walPerGame = GameOutcomeAllTimeCalculator.getWALPerGame(league, **kwargs)

    # AWAL
    awal = AWALAllTimeCalculator.getAWAL(league, **kwargs)
    awalPerGame = AWALAllTimeCalculator.getAWALPerGame(league, **kwargs)
    opponentAWAL = AWALAllTimeCalculator.getOpponentAWAL(league, **kwargs)
    opponentAWALPerGame = AWALAllTimeCalculator.getOpponentAWALPerGame(league, **kwargs)

    # Smart Wins
    smartWins = SmartWinsAllTimeCalculator.getSmartWins(league, **kwargs)
    smartWinsPerGame = SmartWinsAllTimeCalculator.getSmartWinsPerGame(league, **kwargs)
    opponentSmartWins = SmartWinsAllTimeCalculator.getOpponentSmartWins(league, **kwargs)
    opponentSmartWinsPerGame = SmartWinsAllTimeCalculator.getOpponentSmartWinsPerGame(league, **kwargs)

    # Points Scored
    pointsScored = PointsScoredAllTimeCalculator.getPointsScored(league, **kwargs)
    pointsScoredPerGame = PointsScoredAllTimeCalculator.getPointsScoredPerGame(league, **kwargs)
    opponentPointsScored = PointsScoredAllTimeCalculator.getOpponentPointsScored(league, **kwargs)
    opponentPointsScoredPerGame = PointsScoredAllTimeCalculator.getOpponentPointsScoredPerGame(league,
                                                                                               **kwargs)

    # Scoring Share
    scoringShare = ScoringShareAllTimeCalculator.getScoringShare(league, **kwargs)
    opponentScoringShare = ScoringShareAllTimeCalculator.getOpponentScoringShare(league, **kwargs)

    # Single Score
    maxScore = SingleScoreAllTimeCalculator.getMaxScore(league, **kwargs)
    minScore = SingleScoreAllTimeCalculator.getMinScore(league, **kwargs)

    # Scoring Standard Deviation
    scoringStandardDeviation = ScoringStandardDeviationAllTimeCalculator.getScoringStandardDeviation(league,
                                                                                                     **kwargs)

    # Plus Minus
    plusMinus = PlusMinusAllTimeCalculator.getPlusMinus(league, **kwargs)

    # SSL
    teamScore = SSLAllTimeCalculator.getTeamScore(league, **kwargs)
    teamSuccess = SSLAllTimeCalculator.getTeamSuccess(league, **kwargs)
    teamLuck = SSLAllTimeCalculator.getTeamLuck(league, **kwargs)

    return AllTimeStatSheet(wins=wins, losses=losses, ties=ties, winPercentage=winPercentage, wal=wal,
                            walPerGame=walPerGame, awal=awal, awalPerGame=awalPerGame, opponentAWAL=opponentAWAL,
                            opponentAWALPerGame=opponentAWALPerGame, smartWins=smartWins,
                            smartWinsPerGame=smartWinsPerGame, opponentSmartWins=opponentSmartWins,
                            opponentSmartWinsPerGame=opponentSmartWinsPerGame, pointsScored=pointsScored,
                            pointsScoredPerGame=pointsScoredPerGame, opponentPointsScored=opponentPointsScored,
                            opponentPointsScoredPerGame=opponentPointsScoredPerGame, scoringShare=scoringShare,
                            opponentScoringShare=opponentScoringShare, maxScore=maxScore, minScore=minScore,
                            scoringStandardDeviation=scoringStandardDeviation, plusMinus=plusMinus,
                            teamScore=teamScore, teamSuccess=teamSuccess, teamLuck=teamLuck)


def yearStatSheet(year: Year, **kwargs) -> YearStatSheet:
    # Game Outcome
    wins = GameOutcomeYearCalculator.getWins(year, **kwargs)
    losses = GameOutcomeYearCalculator.getLosses(year, **kwargs)
    ties = GameOutcomeYearCalculator.getTies(year, **kwargs)
    winPercentage = GameOutcomeYearCalculator.getWinPercentage(year, **kwargs)
    wal = GameOutcomeYearCalculator.getWAL(year, **kwargs)
    walPerGame = GameOutcomeYearCalculator.getWALPerGame(year, **kwargs)

    # AWAL
    awal = AWALYearCalculator.getAWAL(year, **kwargs)
    awalPerGame = AWALYearCalculator.getAWALPerGame(year, **kwargs)
    opponentAWAL = AWALYearCalculator.getOpponentAWAL(year, **kwargs)
    opponentAWALPerGame = AWALYearCalculator.getOpponentAWALPerGame(year, **kwargs)

    # Smart Wins
    smartWins = SmartWinsYearCalculator.getSmartWins(year, **kwargs)
    smartWinsPerGame = SmartWinsYearCalculator.getSmartWinsPerGame(year, **kwargs)
    opponentSmartWins = SmartWinsYearCalculator.getOpponentSmartWins(year, **kwargs)
    opponentSmartWinsPerGame = SmartWinsYearCalculator.getOpponentSmartWinsPerGame(year, **kwargs)

    # Points Scored
    pointsScored = PointsScoredYearCalculator.getPointsScored(year, **kwargs)
    pointsScoredPerGame = PointsScoredYearCalculator.getPointsScoredPerGame(year, **kwargs)
    opponentPointsScored = PointsScoredYearCalculator.getOpponentPointsScored(year, **kwargs)
    opponentPointsScoredPerGame = PointsScoredYearCalculator.getOpponentPointsScoredPerGame(year, **kwargs)

    # Scoring Share
    scoringShare = ScoringShareYearCalculator.getScoringShare(year, **kwargs)
    opponentScoringShare = ScoringShareYearCalculator.getOpponentScoringShare(year, **kwargs)

    # Single Score
    maxScore = SingleScoreYearCalculator.getMaxScore(year, **kwargs)
    minScore = SingleScoreYearCalculator.getMinScore(year, **kwargs)

    # Scoring Standard Deviation
    scoringStandardDeviation = ScoringStandardDeviationYearCalculator.getScoringStandardDeviation(year, **kwargs)

    # Plus Minus
    plusMinus = PlusMinusYearCalculator.getPlusMinus(year, **kwargs)

    # SSL
    teamScore = SSLYearCalculator.getTeamScore(year, **kwargs)
    teamSuccess = SSLYearCalculator.getTeamSuccess(year, **kwargs)
    teamLuck = SSLYearCalculator.getTeamLuck(year, **kwargs)

    return YearStatSheet(wins=wins, losses=losses, ties=ties, winPercentage=winPercentage, wal=wal,
                         walPerGame=walPerGame, awal=awal, awalPerGame=awalPerGame, opponentAWAL=opponentAWAL,
                         opponentAWALPerGame=opponentAWALPerGame, smartWins=smartWins,
                         smartWinsPerGame=smartWinsPerGame, opponentSmartWins=opponentSmartWins,
                         opponentSmartWinsPerGame=opponentSmartWinsPerGame, pointsScored=pointsScored,
                         pointsScoredPerGame=pointsScoredPerGame, opponentPointsScored=opponentPointsScored,
                         opponentPointsScoredPerGame=opponentPointsScoredPerGame, scoringShare=scoringShare,
                         opponentScoringShare=opponentScoringShare, maxScore=maxScore, minScore=minScore,
                         scoringStandardDeviation=scoringStandardDeviation, plusMinus=plusMinus,
                         teamScore=teamScore, teamSuccess=teamSuccess, teamLuck=teamLuck)
