<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use DB;


class FrezHhzTc99H20200321Controller extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $trazas = DB::table('frez_hhz_tc_99__2020_03_21')
            ->select('frez_hhz_tc_99__2020_03_21.tracebuf')
            ->limit(1)
            ->first();
        $traza = $trazas->tracebuf;
        // $enconde = base8_encode($traza);
        $nuevo = mb_convert_encoding($traza, 'UTF-8', '	BINARY');
        $path = storage_path() . '/app/public/teszt.txt';
        file_put_contents($path, $nuevo);
        //file_put_contents('/app/public/flower.zip', $trazas[0]->tracebuf);
        return response()->json('success', 200);
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        //
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        //
    }
}
