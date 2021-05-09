from teacher import Teacher


def test_class_teacher():
    # input
    name = "Alma"
    years_xp = 15
    is_ma = False
    topics = ["math", "estonian"]

    # process
    teacher = Teacher(name, years_xp, is_master=is_ma, topics=topics)

    # assert
    assert isinstance(teacher, Teacher) is not None


def test_default_values():
    # input
    name = "Ülle"
    years_xp = 10

    # process
    teacher = Teacher(name, years_xp)

    # assert
    assert teacher.name == "Ülle"
    assert teacher.is_master is False
    assert teacher.topics == []


def test_count_topics():
    # input
    name = "Anna"
    years_xp = 1
    is_ma = True
    topics = ["math", "Estonian", "English"]

    # process
    teacher = Teacher(name, years_xp, is_master=is_ma, topics=topics)

    # assert
    assert teacher.topics_taught() == 3
