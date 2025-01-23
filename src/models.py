import numpy as np
import json

def results_to_dict(llm_result):
    return {**llm_result.__dict__,
            'generations': [[gen.__dict__ for gen in gen_list] for gen_list in llm_result.generations]}

def evaluate(llm_evaluator, prompts, cache_path, max_workers: int):

    results = llm_evaluator.batch_generate(prompts, cache_path=cache_path,max_workers=max_workers)
    # if logs:
    #     with open(f"results/{llm_evaluator.model}_{timestamp}.json", "w+") as f:
    #         f.write(json.dumps([results_to_dict(r) for r in results]))
    texts = [r.generations[0][0].text for r in results]
    return results, texts

def get_score_and_re_eval(llm_evaluator, results, prompts, texts, use_json=False, max_retries=3):
    def re_eval(prompts):
        r, t = evaluate(llm_evaluator, prompts, cache_path=None, max_workers=16)
        return r, t

    def get_score(texts):
        scores = []
        errors = []
        if not use_json:
            for i, d in enumerate(texts):
                d = d.split("[[")[-1].strip()
                d = d.split("]]")[0].strip()
                try:
                    scores.append(int(d))
                except Exception as e:
                    print(i, e)
                    errors.append(i)
                    scores.append(0)
        else:
            for i, d in enumerate(texts):
                try:
                    d = d.split('[[SCORE]]')[-1].strip()
                    d = json.loads(d)
                    scores.append(d)
                except Exception as e:
                    print(i, e)
                    errors.append(i)
                    scores.append(0)
        return np.array(scores), np.array(errors)

    scores, errors = get_score(texts)
    
    results = np.array(results)
    texts = np.array(texts)
    prompts = np.array(prompts)
    
    retry = 0
    while(len(errors) > 0 and retry < max_retries):
        re_results, re_texts = re_eval(prompts[errors].tolist())
        re_scores, re_errors = get_score(re_texts)
        scores[errors] = re_scores
        results[errors] = re_results
        texts[errors] = re_texts
        errors = re_errors
        retry += 1

    # with open(f"results/{name_suffix}.json", "a+") as f:
    #     f.write(json.dumps([results_to_dict(r) for r in results]))
    return scores, texts, results
