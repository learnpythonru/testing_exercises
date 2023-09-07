from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    assert change_copy_item('Title') == 'Copy of Title'
    assert change_copy_item('Copy of Title') == 'Copy of Title (2)'
    assert change_copy_item('Copy of') == 'Copy of (2)'
    assert change_copy_item('Дезоксирибонуклеи́новая кислота́ (ДНК) — макромолекула, обеспечивающая хранение и передачу информации') == 'Дезоксирибонуклеи́новая кислота́ (ДНК) — макромолекула, обеспечивающая хранение и передачу информации'
